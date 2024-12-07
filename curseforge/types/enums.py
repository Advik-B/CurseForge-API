from enum import Enum

class CurseCurseCoreApiStatus(Enum):
    PRIVATE = 1
    PUBLIC = 2

class CurseCoreStatus(Enum):
    DRAFT = 1
    TEST = 2
    PENDING_REVIEW = 3
    REJECTED = 4
    APPROVED = 5
    LIVE = 6
