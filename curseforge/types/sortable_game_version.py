from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class CurseSortableGameVersion:
    gameVersionName: str
    gameVersionPadded: str
    gameVersion: str
    gameVersionReleaseDate: datetime
    gameVersionTypeId: int = field(default=None)

    @staticmethod
    def from_dict(data: dict):
        return CurseSortableGameVersion(
            gameVersionName=data["gameVersionName"],
            gameVersionPadded=data["gameVersionPadded"],
            gameVersion=data["gameVersion"],
            gameVersionReleaseDate=datetime.fromisoformat(data["gameVersionReleaseDate"]),
            gameVersionTypeId=data.get("gameVersionTypeId", None)
        )