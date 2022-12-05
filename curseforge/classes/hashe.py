from dataclasses import dataclass
from .base import CurseObject

@dataclass
class CurseHash(CurseObject):
    value: str
    algo: int

    @staticmethod
    def from_dict(data: dict):
        return CurseHash(
            value=data.get("value"),
            algo=data.get("algo")
        )
