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


    @staticmethod
    def from_dict(data: dict):
        return CurseGame(
            id=data["id"],
            name=data["name"],
            slug=data["slug"],
            dateModified=datetime.fromisoformat(data["dateModified"]),
            assets=CurseAsset.from_dict(data["assets"]),
            status=data["status"],
            apiStatus=data["apiStatus"]
        )

    @staticmethod
    def list(api: CurseForgeAPI):
        return [CurseGame.from_dict(game) for game in api.fetch("/v1/games")]

    @staticmethod
    def from_id(game_id: int, api: CurseForgeAPI):
        return CurseGame.from_dict(api.fetch(f"/v1/games/{game_id}"))