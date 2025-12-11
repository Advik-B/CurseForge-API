from dataclasses import dataclass
from .base import CurseObject

@dataclass
class CurseImage(CurseObject):
    id: int
    modId: int
    title: str
    description: str
    thumbnail_url: str
    url: str

    @staticmethod
    def from_dict(data: dict):
        return CurseImage(
            id=data.get("id", 0),
            modId=data.get("modId", 0),
            title=data.get("title", ""),
            description=data.get("description", ""),
            thumbnail_url=data.get("thumbnailUrl", ""),
            url=data.get("url", "")
        )
