from typing import List, AnyStr
from dataclasses import dataclass

@dataclass
class CurseVersion:
    type: int
    versions: List[AnyStr]

    @staticmethod
    def from_dict(data: dict):
        return CurseVersion(
            type=data["type"],
            versions=data["versions"]
        )

@dataclass
class CurseVersions:
    _versions: List[CurseVersion]

    @staticmethod
    def from_dict(data: dict):
        return CurseVersions(
            _versions=[CurseVersion.from_dict(version) for version in data]
        )

    __getitem__ = lambda self, index: self._versions[index]
    __iter__ = lambda self: iter(self._versions)
    __len__ = lambda self: len(self._versions)
    __repr__ = lambda self: repr(self._versions)