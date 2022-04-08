class FacingError(Exception):
    """Custom exception regarding the cardinal compass points"""
    pass


class MoveError(Exception):
    """Custom exception if the requested move is invalid"""
    pass


class InvalidTileCountError(Exception):
    """Custom exception if tile count is negative"""
    pass
