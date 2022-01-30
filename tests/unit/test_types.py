from freezegun import freeze_time

from gateau_api.types import GameEvent


def test_game_event_default_time():
    frozen_time = "2020-10-11T10:11:12Z"

    with freeze_time(frozen_time):
        event = GameEvent(meaning="a", value=123, player_id="b")

    assert event.timestamp == frozen_time
