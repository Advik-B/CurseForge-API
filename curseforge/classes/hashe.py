from dataclasses import dataclass
from .base import CurseObject

@dataclass
class Hash(CurseObject):
    value: str
    algo: int
