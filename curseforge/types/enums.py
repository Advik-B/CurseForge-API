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

class ModStatus(Enum):
    NEW = 1
    CHANGES_REQUIRED = 2
    UNDER_SOFT_REVIEW = 3
    APPROVED = 4
    REJECTED = 5
    CHANGES_MADE = 6
    INACTIVE = 7
    ABANDONED = 8
    DELETED = 9
    UNDER_REVIEW = 10

class ModsSearchSortField(Enum):
    FEATURED = 1
    POPULARITY = 2
    LAST_UPDATED = 3
    NAME = 4
    AUTHOR = 5
    TOTAL_DOWNLOADS = 6
    CATEGORY = 7
    GAME_VERSION = 8
    EARLY_ACCESS = 9
    FEATURED_RELEASED = 10
    RELEASED_DATE = 11
    RATING = 12

class ModLoaderType(Enum):
    ANY = 0
    FORGE = 1
    CAULDRON = 2
    LITELOADER = 3
    FABRIC = 4
    QUILT = 5
    NEOFORGE = 6