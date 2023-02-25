from dataclasses import dataclass
from .base import CurseObject

@dataclass
class CurseModFileManifest(CurseObject):
    project_id: int
    file_id: int
    required: bool

    @staticmethod
    def from_dict(data: dict):
        return CurseModFileManifest(
            project_id=data.get("projectID"),
            file_id=data.get("fileID"),
            required=data.get("required")
        )

@dataclass
class CurseManifest(CurseObject):
    manifest_type: str
    manifest_version: int
    name: str
    version: str
    author: list[str]
    files: list[CurseModFileManifest]
    overrides: str

    @staticmethod
    def from_dict(data: dict):
        return CurseManifest(
            manifest_type=data.get("manifestType"),
            manifest_version=data.get("manifestVersion"),
            name=data.get("name"),
            version=data.get("version"),
            author=data.get("author"),
            files=[CurseModFileManifest.from_dict(file) for file in data.get("files")],
            overrides=data.get("overrides")
        )
