class GateauApiException(Exception):
    """
    Base exception for Gateau API
    """


class PlayerNotFound(GateauApiException):
    """
    Expected player not found
    """
