from dataclasses import dataclass
from .base import CurseObject

@dataclass
class CurseHash(CurseObject):
    value: str
    algo: int
