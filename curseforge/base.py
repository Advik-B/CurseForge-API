from requests import get, post
from dataclasses import dataclass
from typing import Generator
from .classes import CurseGame, CurseGameAssets, CurseCategory, CurseMod

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


    def game(self, game_id: int) -> CurseGame:
        if self.cache:
            temp = self.cache_obj.get(f"game_{game_id}")
            if temp is not None:
                _game = temp
                del temp
            else:
                _game = self.fetch(f"games/{game_id}")
                self.cache_obj.set(f"game_{game_id}", _game)
            return CurseGame.from_dict(_game)

        else:
            game_ = self.fetch(f"games/{game_id}")
            return CurseGame.from_dict(game_)

    def games(self) -> Generator[CurseGame, CurseGame, ...]:
        """Returns a generator of CurseGame objects to iterate over live"""
        for game in self.fetch("games"):
            if self.cache:
                self.cache_obj.set(f"game_{game.get('id')}", game)
            yield CurseGame(
                id=game.get("id"),
                name=game.get("name"),
                slug=game.get("slug"),
                assets=CurseGameAssets(*game.get("assets")),
                status=game.get("status"),
                api_status=game.get("api_status"),
                date_modified=game.get("date_modified"),
            )

    def game_versions(self, game_id: int):
        return self.fetch(f"game/{game_id}/versions")

    def categories(self, game_id: int) -> Generator[CurseCategory, CurseCategory, ...]:
        for category in self.fetch("categories", {"gameId": game_id}):
            self.cache_obj.set(f"category_{category.get('id')}", category)
            yield CurseCategory.from_dict(category)

    def addon(self, addon_id: int) -> CurseMod:
        if self.cache:
            temp = self.cache_obj.get(f"addon_{addon_id}")
            if temp is not None:
                _addon = temp
                del temp
            else:
                _addon = self.fetch(f"addon/{addon_id}")
                self.cache_obj.set(f"addon_{addon_id}", _addon)
            return CurseMod.from_dict(_addon)

        else:
            addon_ = self.fetch(f"addon/{addon_id}")
            return CurseMod.from_dict(addon_)

    def clean_cache(self):
        if self.cache:
            self.cache_obj.clear()
            self.cache_obj.close()