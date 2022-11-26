from dataclasses import dataclass
from .base import CurseObject

@dataclass
class GameAssets(CurseObject):
    icon_url: str
    tile_url: str
    cover_url: str

@dataclass
class Game(CurseObject):
    id: int
    name: str
    slug: str
    assets: GameAssets
    status: int
    api_status: int
    date_modified: str