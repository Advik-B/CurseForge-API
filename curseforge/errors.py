class CurseForgeError(Exception):
    """Base exception for all CurseForge errors."""
    pass


class CurseResponseIsNotJSON(CurseForgeError):
    """Raised when the response is not JSON."""
    pass