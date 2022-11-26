from dataclasses import dataclass
from .base import CurseObject

@dataclass
class Image(CurseObject):
    id: int
    modId: int
    title: str
    description: str
    thumbnail_url: str
    url: str

