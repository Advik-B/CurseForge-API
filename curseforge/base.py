from requests import get, post
from dataclasses import dataclass
from typing import Generator, Union
from .classes import (
    CurseGame,
    CurseGameAssets,
    CurseCategory,
    CurseMod,
    CurseModFile,
    CurseModFileManifest
)
from urllib3.exceptions import InsecureRequestWarning
from warnings import simplefilter

from diskcache import Cache

BASE_URL = "http://api.curseforge.com"
MOD_BASE_URL = "https://edge.forgecdn.net/files/%(file_id_1)s/%(file_id_2)s/%(file_name)s"


@dataclass
class CurseClient:
    api_key: str
    version: str = "v1"
    cache: bool = False
    cache_dir: str = "cache/curseforge"

    def __post_init__(self):
        if self.cache:
            self.cache_obj = Cache(self.cache_dir)

    def fetch_raw(self, url: str, params: dict = None, method: str = "GET"):
        if params is None:
            params = {}

        simplefilter("ignore", InsecureRequestWarning)
        method = method.casefold()
        if method == "get":
            return get(
                f"{BASE_URL}/{self.version}/{url}",
                headers={
                    "X-API-Key": self.api_key,
                    "Accept": "application/json"
                },
                params=params,
                verify=False
            )
        elif method == "post":
            return post(
                f"{BASE_URL}/{self.version}/{url}",
                headers={
                    "X-API-Key": self.api_key,
                    "Accept": "application/json"
                },
                params=params,
                verify=False
            )
        # We are now safe to reset the filter
        # We are resetting the filter to default because it can affect other libraries and the user's code
        simplefilter("default", InsecureRequestWarning)

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
        return CurseGame.from_dict(self.fetch(f"games/{game_id}"))

    def games(self) -> Generator[CurseGame, CurseGame, None]:
        """Returns a generator of CurseGame objects to iterate over (live)"""
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

    def game_versions(self, game_id: int) -> Union[dict, list]:
        return self.fetch(f"game/{game_id}/versions")

    def categories(self, game_id: int) -> Generator[CurseCategory, CurseCategory, None]:
        for category in self.fetch("categories", {"gameId": game_id}):
            self.cache_obj.set(f"category_{category.get('id')}", category)
            yield CurseCategory.from_dict(category)

    def addon(self, addon_id: int) -> CurseMod:
        return CurseMod.from_dict(self.fetch(f"addon/{addon_id}"))

    def clean_cache(self):
        if self.cache:
            self.cache_obj.clear()

    def get_mod_files(self, addon_id: int):
        for file in self.fetch(f"addon/{addon_id}/files"):
            yield CurseModFile.from_dict(file)

    def get_mod_file(self, addon_id: int, file_id: int,
                     on_guess: callable = lambda addon_id, file_id: None) -> CurseModFile:
        mod = CurseModFile.from_dict(self.fetch(f"mods/{addon_id}/files/{file_id}"))
        if mod.download_url is None:
            # Guess the download url
            on_guess(addon_id, file_id)
            file_id = str(file_id)[1:] if str(file_id).startswith("0") else str(file_id)
            file_id_1 = file_id[:4]
            file_id_2 = file_id[4:7]
            mod.download_url = MOD_BASE_URL % {
                "file_id_1": file_id_1,
                "file_id_2": file_id_2,
                "file_name": mod.file_name
            }
        return mod

    def close_cache(self):
        if self.cache:
            self.cache_obj.close()

    def manifest_to_modfile(self, manifest: CurseModFileManifest) -> CurseModFile:
        """
        Converts a CurseModFileManifest object to a CurseModFile object using the `get_mod_file` method
        :param manifest: CurseModFileManifest object
        :return: CurseModFile object
        """
        return self.get_mod_file(manifest.project_id, manifest.file_id)



