"""
Constants for the CurseForge API wrapper.

This module provides convenient constants for common game IDs and sort fields
to make the API more user-friendly and readable.
"""


class Games:
    """Common game IDs for CurseForge API."""
    MINECRAFT = 432
    WORLD_OF_WARCRAFT = 1
    KERBAL_SPACE_PROGRAM = 4401
    WORLD_OF_TANKS = 4328
    THE_SIMS_4 = 4383
    CITIES_SKYLINES = 4364
    FALLOUT_4 = 4187
    SKYRIM = 4187
    CYBERPUNK_2077 = 3982
    VALHEIM = 4656


class SORT_FIELDS:
    """Sort field constants for search operations."""
    FEATURED = 1
    POPULARITY = 2 
    LAST_UPDATED = 3
    NAME = 4
    AUTHOR = 5
    TOTAL_DOWNLOADS = 6
    CATEGORY = 7
    GAME_VERSION = 8


class SORT_ORDER:
    """Sort order constants."""
    ASCENDING = "asc"
    DESCENDING = "desc"
    ASC = "asc"
    DESC = "desc"