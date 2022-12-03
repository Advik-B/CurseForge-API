from dataclasses import dataclass
from .base import CurseObject

@dataclass
class CurseCategory(CurseObject):
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

    @staticmethod
    def from_dict(data: dict) -> "CurseCategory":
        return CurseCategory(
            id=data.get("id"),
            game_id=data.get("gameId"),
            name=data.get("name"),
            slug=data.get("slug"),
            url=data.get("url"),
            icon_url=data.get("iconUrl"),
            date_modified=data.get("dateModified"),
            is_Class=data.get("isClass"),
            class_id=data.get("classId"),
            parentCategory_id=data.get("parentCategoryId"),
            displayIndex=data.get("displayIndex"),
        )