{
      "id": 0,
      "gameId": 0,
      "name": "string",
      "slug": "string",
      "url": "string",
      "iconUrl": "string",
      "dateModified": "2019-08-24T14:15:22Z",
      "isClass": True,
      "classId": 0,
      "parentCategoryId": 0,
      "displayIndex": 0
}

from dataclasses import dataclass
from datetime import datetime

@dataclass
class CurseCategory:
    id: int
    gameId: int
    name: str
    slug: str
    url: str
    iconUrl: str
    dateModified: datetime
    isClass: bool
    classId: int
    parentCategoryId: int
    displayIndex: int


    @staticmethod
    def from_dict(data: dict):
        return CurseCategory(
            id=data["id"],
            gameId=data["gameId"],
            name=data["name"],
            slug=data["slug"],
            url=data["url"],
            iconUrl=data["iconUrl"],
            dateModified=datetime.fromisoformat(data["dateModified"]),
            isClass=data["isClass"],
            classId=data["classId"],
            parentCategoryId=data["parentCategoryId"],
            displayIndex=data["displayIndex"]
        )
    
    @staticmethod
    def s(api) -> "CurseCategories":
        return CurseCategories.from_dict(api.fetch("/v1/categories"))


@dataclass
class CurseCategories:
    _categories: list

    @staticmethod
    def from_dict(data: dict):
        return CurseCategories(
            _categories=[CurseCategory.from_dict(category) for category in data]
        )

    __getitem__ = lambda self, index: self._categories[index]
    __iter__ = lambda self: iter(self._categories)
    __len__ = lambda self: len(self._categories)
    __repr__ = lambda self: repr(self._categories)