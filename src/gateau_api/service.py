"""
Database structure:

{
    "games": {
        "{gameId}": {
            "players": {
                "{player-uid}": {
                    "uid": "{player-uid}",
                    "cartridge": "pokemon_red",
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
    }
}
"""

from typing import List, Set

from pyrebase import initialize_app
from pyrebase.pyrebase import Database

from gateau_api.constants import (
    FIREBASE_API_KEY,
    FIREBASE_AUTH_DOMAIN,
    FIREBASE_DATABASE_URL,
    FIREBASE_STORAGE_BUCKET,
)
from gateau_api.game_ram.cartridge_info import ChangeMeaning
from gateau_api.game_ram.carts import cart_info
from gateau_api.types import GameEvent, Player, RamChangeInfo


class GateauFirebaseService:
    """
    Service for Gateau games stored in Firebase's realtime database
    """

    def __init__(self):
        firebase = initialize_app(
            {
                "databaseURL": FIREBASE_DATABASE_URL,
                "apiKey": FIREBASE_API_KEY,
                "authDomain": FIREBASE_AUTH_DOMAIN,
                "storageBucket": FIREBASE_STORAGE_BUCKET,
            }
        )
        self.root = firebase.database()

    def games_db(self) -> Database:
        """
        Reference to the games db
        """
        return self.root.child("games")

    def game_db(self, game_id: str) -> Database:
        """
        Child for a specific game
        """
        return self.games_db().child(game_id)

    def players_db(self, game_id: str) -> Database:
        """
        Child for players
        """
        return self.game_db(game_id=game_id).child("players")

    def player_db(self, game_id: str, player_id: str) -> Database:
        """
        Child for a specific player
        """
        return self.players_db(game_id).child(player_id)

    def events_db(self, game_id: str) -> Database:
        """
        Child for events
        """
        return self.game_db(game_id=game_id).child("events")

    def subscriptions_db(self, game_id: str) -> Database:
        """
        Child for subscriptions
        """
        return self.game_db(game_id=game_id).child("subscriptions")

    def get_player(self, game_id: str, player_id: str) -> Player:
        """
        Get a player
        """
        db = self.player_db(game_id=game_id, player_id=player_id)
        return Player.parse_obj(db.get().val())

    def set_player(self, game_id: str, player: Player):
        """
        Set a player in the DB
        """
        db = self.players_db(game_id=game_id)
        db.child(player.uid).set(player.dict())

    def get_subscriptions(self, game_id) -> Set[str]:
        """
        Get subscriptions by meaning
        """
        db = self.subscriptions_db(game_id=game_id)
        subscriptions = db.get().val()
        return {key for key, value in subscriptions.items() if value}

    def add_subscriptions(self, game_id: str, meanings: Set[str]):
        """
        Idempotently add some subscriptions to the game
        """
        for meaning in meanings:
            db = self.subscriptions_db(game_id=game_id)
            db.child(meaning).set(True)

    def get_events(self, game_id: str) -> List[GameEvent]:
        """
        Get events from a game, in chronological order
        """
        db = self.events_db(game_id=game_id)
        events = [GameEvent.parse_obj(event) for event in db.get().val().values()]
        return sorted(events, key=lambda e: e.timestamp)

    def add_event(self, game_id: str, event: GameEvent):
        """
        Push a new game event
        """
        db = self.events_db(game_id=game_id)
        db.push(event.dict())

    def get_ram_subscriptions(self, game_id: str, player_id: str) -> Set[int]:
        """
        Get the RAM addresses a player should subscribe to, according to the
        cartridge they're using
        """
        subscriptions = self.get_subscriptions(game_id=game_id)
        player = self.get_player(game_id=game_id, player_id=player_id)
        info = cart_info(player.cartridge)
        ram_addresses = {info.byte_for_meaning(meaning) for meaning in subscriptions}

        return ram_addresses

    def handle_ram(self, game_id: str, player_id: str, change_info: RamChangeInfo):
        """
        Handle a RAM change event
        """
        player = self.get_player(game_id=game_id, player_id=player_id)
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
                self.add_event(game_id=game_id, event=event)
