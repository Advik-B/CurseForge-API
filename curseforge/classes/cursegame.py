from dataclasses import dataclass
from .base import CurseObject

@dataclass
class CurseGameAssets(CurseObject):
    icon_url: str
    tile_url: str
    cover_url: str

@dataclass
class CurseGame(CurseObject):
    id: int
    name: str
    slug: str
    assets: CurseGameAssets
    status: int
    api_status: int
    date_modified: str

    @staticmethod
    def from_dict(data: dict):
        return CurseGame(
            id=data.get("id"),
            name=data.get("name"),
            slug=data.get("slug"),
            assets=CurseGameAssets(*data.get("assets").values()),
            status=data.get("status"),
            api_status=data.get("apiStatus"),
            date_modified=data.get("dateModified"),
        )