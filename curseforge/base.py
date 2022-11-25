from requests import get
from dataclasses import dataclass
from curseclasses import CurseGame

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
            assets=_game["assets"],
            status=_game["status"],
            api_status=_game["api_status"],
            date_modified=_game["date_modified"],
        )



