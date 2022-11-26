from requests import get, post
from dataclasses import dataclass
from typing import Generator
from .classes import Game, GameAssets, Category

BASE_URL = "http://api.curseforge.com"


@dataclass
class CurseClient:
    api_key: str
    version: str = "v1"

    def fetch(self, url: str, params: dict = None, method: str = "GET"):
        if params is None:
            params = {}

        method = method.casefold()
        if method == "get":
            return get(
                f"{BASE_URL}/{self.version}/{url}",
                headers={
                    "X-API-Key": self.api_key,
                    "Accept": "application/json"
                },
                params=params
            ).json()["data"]
        elif method == "post":
                return post(
                    f"{BASE_URL}/{self.version}/{url}",
                    headers={
                        "X-API-Key": self.api_key,
                        "Accept": "application/json"
                    },
                    params=params
                ).json()["data"]

    def game(self, game_id: int) -> Game:
        _game = self.fetch(f"games/{game_id}")
        return Game(
            id=_game["id"],
            name=_game["name"],
            slug=_game["slug"],
            url=_game.get("url"),
            assets=GameAssets(*_game["assets"]),
            status=_game["status"],
            api_status=_game.get("api_status"),
            date_modified=_game("date_modified"),
        )

    def games(self) -> Generator[Game, Game, ...]:
        """Returns a generator of CurseGame objects to iterate over live"""
        for game in self.fetch("games"):
            yield Game(
                id=game["id"],
                name=game["name"],
                slug=game["slug"],
                url=game["url"],
                assets=GameAssets(*game["assets"]),
                status=game["status"],
                api_status=game["api_status"],
                date_modified=game["date_modified"],
            )

    def game_versions(self, game_id: int):
        return self.fetch(f"game/{game_id}/versions")

    def categories(self, game_id: int) -> Generator[Category, Category, ...]:
        for category in self.fetch("categories", {"gameId": game_id}):
            yield Category(
                id=category["id"],
                game_id=category["gameId"],
                name=category["name"],
                slug=category["slug"],
                url=category["url"],
                icon_url=category["iconUrl"],
                date_modified=category["dateModified"],
                is_Class=category["isClass"],
                class_id=category["classId"],
                parentCategory_id=category["parentCategoryId"],
                displayIndex=category["displayIndex"],
            )
