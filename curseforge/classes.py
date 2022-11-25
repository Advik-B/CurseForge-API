from dataclasses import dataclass

@dataclass
class CurseGameAssets:
    icon_url: str
    tile_url: str
    cover_url: str

@dataclass
class CurseGame:
    id: int
    name: str
    slug: str
    url: str
    assets: CurseGameAssets
    status: int
    api_status: int
    date_modified: str

@dataclass
class CurseGameList:
    games: list[CurseGame]