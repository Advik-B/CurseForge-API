from requests import get, post
from dataclasses import dataclass
from typing import Generator
from .classes import Game, GameAssets, Category
import diskcache

BASE_URL = "http://api.curseforge.com"


@dataclass
class CurseClient:
    api_key: str
    version: str = "v1"
    cache: bool = False
    cache_dir: str = "cache"

    def __post_init__(self):
        if self.cache:
            self.cache_obj = diskcache.Cache(self.cache_dir)

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
        if self.cache and self.cache_obj.get(f"game_{game_id}") is not None:
            _game = self.cache_obj.get(f"game_{game_id}")
        else:
            _game = self.fetch(f"game/{game_id}")

        return Game(
            id=_game.get("id"),
            name=_game.get("name"),
            slug=_game.get("slug"),
            assets=GameAssets(*_game.get("assets")),
            status=_game.get("status"),
            api_status=_game.get("apiStatus"),
            date_modified=_game.get("dateModified"),
        )

    def games(self) -> Generator[Game, Game, ...]:
        """Returns a generator of CurseGame objects to iterate over live"""
        for game in self.fetch("games"):
            self.cache_obj.set(f"game_{game.get('id')}", game)
            yield Game(
                id=game.get("id"),
                name=game.get("name"),
                slug=game.get("slug"),
                assets=GameAssets(*game.get("assets")),
                status=game.get("status"),
                api_status=game.get("api_status"),
                date_modified=game.get("date_modified"),
            )

    def game_versions(self, game_id: int):
        return self.fetch(f"game/{game_id}/versions")

    def categories(self, game_id: int) -> Generator[Category, Category, ...]:
        for category in self.fetch("categories", {"gameId": game_id}):
            self.cache_obj.set(f"category_{category.get('id')}", category)
            yield Category(
                id=category.get("id"),
                game_id=category.get("gameId"),
                name=category.get("name"),
                slug=category.get("slug"),
                url=category.get("url"),
                icon_url=category.get("iconUrl"),
                date_modified=category.get("dateModified"),
                is_Class=category.get("isClass"),
                class_id=category.get("classId"),
                parentCategory_id=category.get("parentCategoryId"),
                displayIndex=category.get("displayIndex"),
            )
