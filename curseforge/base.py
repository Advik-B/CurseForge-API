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

    def fetch_raw(self, url: str, params: dict = None, method: str = "GET"):
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
            )
        elif method == "post":
                return post(
                    f"{BASE_URL}/{self.version}/{url}",
                    headers={
                        "X-API-Key": self.api_key,
                        "Accept": "application/json"
                    },
                    params=params
                )

    def fetch(self, url: str, params: dict = None, method: str = "GET") -> dict:
        if params is None:
            params = {}

        if self.cache:
            temp = self.cache_obj.get(url)
        if self.cache and temp is not None:
            return temp["data"]

        response = self.fetch_raw(url, params, method)
        if response.status_code == 200:
            data = response.json()
            if self.cache:
                self.cache_obj.set(url, data)
            return data["data"]


    def game(self, game_id: int) -> Game:
        if self.cache:
            temp = self.cache_obj.get(f"game_{game_id}")
            if temp is not None:
                _game = temp
                del temp
            else:
                _game = self.fetch(f"games/{game_id}")
                self.cache_obj.set(f"game_{game_id}", _game)
            return Game.from_dict(_game)

        else:
            game_ = self.fetch(f"games/{game_id}")
            return Game.from_dict(game_)

    def games(self) -> Generator[Game, Game, ...]:
        """Returns a generator of CurseGame objects to iterate over live"""
        for game in self.fetch("games"):
            if self.cache:
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

    def clean_cache(self):
        if self.cache:
            self.cache_obj.clear()
            self.cache_obj.close()