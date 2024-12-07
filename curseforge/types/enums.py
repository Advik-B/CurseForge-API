from enum import Enum

class CoreApiStatus(Enum):
    PRIVATE = 1
    PUBLIC = 2

class CoreStatus(Enum):
    DRAFT = 1
    TEST = 2
    PENDING_REVIEW = 3
    REJECTED = 4
    APPROVED = 5
    LIVE = 6
