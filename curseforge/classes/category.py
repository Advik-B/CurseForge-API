from dataclasses import dataclass
from .base import CurseObject

@dataclass
class Category(CurseObject):
    id: int
    game_id: int
    name: str
    slug: str
    url: str
    icon_url: str
    date_modified: str
    is_Class: bool
    class_id: int
    parentCategory_id: int
    displayIndex: int

