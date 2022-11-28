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

    @staticmethod
    def from_dict(data: dict):
        return Game(
            id=data.get("id"),
            name=data.get("name"),
            slug=data.get("slug"),
            assets=GameAssets('a', 'b', 'c'),
            status=data.get("status"),
            api_status=data.get("apiStatus"),
            date_modified=data.get("dateModified"),
        )