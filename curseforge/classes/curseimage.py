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

