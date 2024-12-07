from ..engine import CurseForgeAPI
from .assets import CurseAsset
from datetime import datetime
from dataclasses import dataclass

@dataclass
class CurseGame:
    id: int
    name: str
    slug: str
    dateModified: datetime
    assets: CurseAsset
    status: int
    apiStatus: int
