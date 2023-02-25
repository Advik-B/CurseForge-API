from dataclasses import dataclass
from .base import CurseObject
from .cursemod import CurseModFile, CurseMod

@dataclass
class CurseModFileManifest(CurseObject):
    project_id: int
    file_id: int
    required: bool

@dataclass
class CurseManifest(CurseObject):
    manifest_type: str
    manifest_version: int
    name: str
    version: str
    author: list[str]
    files: list[CurseModFileManifest]
    overrides: str
