"""
Database structure:

{
    "games": {
        "{gameId}": {
            "players": {
                "{player-uid}": {
                    "uid": "{player-uid}",
                    "cartridge": "pokemon_red",
                    "color": "#F33F19",
                }
            },
            "events": {
                "{random-unique-id}": {
                    "meaning": "Pikachu owned",
                    "value": true,
                    "playerName": "aaa",
                    "timestamp": "2020-10-10T10:20:30Z",
                }
            },
            "subscriptions": {
                "{meaning}": true,
            },
        }
    },
    "desktopJoinTokens": {
        "{player-uid}": "some-game-id",
    }
}
"""

from dataclasses import dataclass, field
from typing import List, Set

from firebasil.auth import AuthClient
from firebasil.rtdb import Rtdb, RtdbNode

from gateau_api.constants import FIREBASE_API_KEY, FIREBASE_DATABASE_URL
from gateau_api.exceptions import PlayerNotFound
from gateau_api.game_ram.cartridge_info import ChangeMeaning
from gateau_api.game_ram.carts import cart_info
from gateau_api.types import GameEvent, Player, RamChangeInfo


@dataclass
class GateauFirebaseService:
    """
    Service for Gateau games stored in Firebase's realtime database
    """

    #: User ID token
    id_token: str

    _rtdb: Rtdb = field(
        init=False,
        repr=False,
        hash=False,
        compare=False,
    )

    db_root: RtdbNode = field(
        init=False,
        repr=False,
        hash=False,
        compare=False,
    )

    auth_client: AuthClient = field(
        init=False,
        repr=False,
        hash=False,
        compare=False,
    )

    async def __aenter__(self):
        self._rtdb = Rtdb(
            database_url=FIREBASE_DATABASE_URL,
            id_token=self.id_token,
        )
        self.db_root = await self._rtdb.__aenter__()

        self.auth_client = await AuthClient(api_key=FIREBASE_API_KEY).__aenter__()

        return self

    async def __aexit__(self, *err):
        self.db_root = None

        await self.auth_client.__aexit__(*err)
        await self._rtdb.__aexit__(*err)

        self.auth_client = None
        self._rtdb = None

    def games_db(self) -> RtdbNode:
        """
        Reference to the games db
        """
        return self.db_root / "games"

    def game_db(self, game_id: str) -> RtdbNode:
        """
        Child for a specific game
        """
        return self.games_db() / game_id

    def players_db(self, game_id: str) -> RtdbNode:
        """
        Child for players
        """
        return self.game_db(game_id=game_id) / "players"

    def player_db(self, game_id: str, player_id: str) -> RtdbNode:
        """
        Child for a specific player
        """
        return self.players_db(game_id) / player_id

    def events_db(self, game_id: str) -> RtdbNode:
        """
        Child for events
        """
        return self.game_db(game_id=game_id) / "events"

    def subscriptions_db(self, game_id: str) -> RtdbNode:
        """
        Child for subscriptions
        """
        return self.game_db(game_id=game_id) / "subscriptions"

    async def get_player(self, game_id: str, player_id: str) -> Player:
        """
        Get a player
        """
        db = self.player_db(game_id=game_id, player_id=player_id)
        result = await db.get()
        if result is None:
            raise PlayerNotFound(f"No player with UID {player_id} in game {game_id}")
        return Player.parse_obj(result)

    async def join_game(self, game_id: str, player: Player):
        """
        Set a player in the DB
        """
        db = self.players_db(game_id=game_id)

        await (db / player.uid).set(player.dict())

    async def remove_player(self, game_id: str, player_id: str):
        """
        Remove a player from a game
        """
        db = self.players_db(game_id=game_id)
        await (db / player_id).delete()

    async def get_subscriptions(self, game_id) -> Set[str]:
        """
        Get subscriptions by meaning
        """
        db = self.subscriptions_db(game_id=game_id)
        subscriptions = await db.get()
        return {key for key, value in subscriptions.items() if value}

    async def add_subscriptions(self, game_id: str, meanings: Set[str]):
        """
        Idempotently add some subscriptions to the game
        """
        for meaning in meanings:
            db = self.subscriptions_db(game_id=game_id)
            await (db / meaning).set(True)

    async def get_events(self, game_id: str) -> List[GameEvent]:
        """
        Get events from a game, in chronological order
        """
        db = self.events_db(game_id=game_id)
        events_raw = await db.get()
        events = [GameEvent.parse_obj(event) for event in events_raw.values()]
        return sorted(events, key=lambda e: e.timestamp)

    async def add_event(self, game_id: str, event: GameEvent) -> None:
        """
        Push a new game event
        """
        db = self.events_db(game_id=game_id)
        await db.push(event.dict())

    async def get_ram_subscriptions(self, game_id: str, player_id: str) -> Set[int]:
        """
        Get the RAM addresses a player should subscribe to, according to the
        cartridge they're using
        """
        subscriptions = await self.get_subscriptions(game_id=game_id)
        player = await self.get_player(game_id=game_id, player_id=player_id)
        if not player:
            raise PlayerNotFound(f"No player with UID {player_id} in game {game_id}")
        info = cart_info(player.cartridge)
        ram_addresses = {info.byte_for_meaning(meaning) for meaning in subscriptions}

        return ram_addresses

    async def handle_ram(
        self,
        game_id: str,
        player_id: str,
        change_info: RamChangeInfo,
    ) -> None:
        """
        Handle a RAM change event
        """
        player = await self.get_player(game_id=game_id, player_id=player_id)
        info = cart_info(player.cartridge)
        for ram_event in change_info.events:
            updates: List[ChangeMeaning] = info.meaning_for_byte_change(
                address=ram_event.location,
                old_value=ram_event.old,
                new_value=ram_event.new,
            )
            for update in updates:
                event = GameEvent(
                    meaning=update.meaning,
                    value=update.value,
                    player_id=player.uid,
                )
                await self.add_event(game_id=game_id, event=event)
