from requests import get
from dataclasses import dataclass
from classes import CurseGame, CurseGameAssets

BASE_URL = "https://api.curseforge.com"


@dataclass
class CurseClient:
    api_key: str
    version: str = "v1"

    def fetch(self, url: str):
        return get(
            f"{BASE_URL}/{self.version}/{url}",
            headers={
                "X-API-Key": self.api_key,
                "Accept": "application/json"
            }
        ).json()["data"]

    def game(self, game_id: int):
        _game = self.fetch(f"games/{game_id}")
        return CurseGame(
            id=_game["id"],
            name=_game["name"],
            slug=_game["slug"],
            url=_game["url"],
            assets=CurseGameAssets(*_game["assets"]),
            status=_game["status"],
            api_status=_game["api_status"],
            date_modified=_game["date_modified"],
        )

    def games(self) -> tuple[CurseGame]:
        """Returns a tuple of CurseGame objects"""
        # We are using a tuple here because we don't want to allow the user to modify the list
        return tuple(
                CurseGame(
                    id=game["id"],
                    name=game["name"],
                    slug=game["slug"],
                    url=game["url"],
                    assets=CurseGameAssets(*game["assets"]),
                    status=game["status"],
                    api_status=game["api_status"],
                    date_modified=game["date_modified"],
                )
                for game in self.fetch("games")
        )
