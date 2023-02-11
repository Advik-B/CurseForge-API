from dataclasses import dataclass
from .base import CurseObject

@dataclass
class CurseManifest(CurseObject):
    manifest_type: str
    manifest_version: int
    name: str
    version: str

