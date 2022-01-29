"""
Database structure:

{
    "games": {
        "{gameId}": {
            "players": {
                "{player-uid}": {
                    "uid": "player-uid",
                    "name": "aaa",
                    "cartridge": "pokemon_red",
                }
            },
            "goals": {
                "random-unique-key": {
                    "kind": "bbb",
                    "claimed_by": {
                        "player-uid": true,
                    },
                }
            },
            "subscriptions": {
                "{player-uid}": [
                    0x1234,
                    0xABCD,
                ]
            }
        }
    }
}
"""

from firebase_admin import db
from firebase_admin.db import Reference

from gateau_api.types import Player, RamChangeInfo


class GateauFirebaseService:
    """
    Service for Gateau games stored in Firebase's realtime database
    """

    def __init__(self):
        self.root = db.reference("/")

    def games_db(self) -> Reference:
        """
        Reference to the games db
        """
        return self.root.child("games")

    def game_db(self, game_id: str) -> Reference:
        """
        Child for a specific game
        """
        return self.games_db().child(game_id)

    def get_goals(self, game_id: str):
        """
        Get goals for a specific game
        """
        ...

    def handle_ram(self, change_info: RamChangeInfo, player: Player):
        """
        Handle a RAM change event
        """
        for event in change_info.events:
            pass
