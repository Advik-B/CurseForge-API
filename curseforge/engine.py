from requests import get
from requests.exceptions import RequestException, JSONDecodeError
from diskcache import Cache
from urllib.parse import urljoin

from .errors import CurseForgeError, CurseResponseIsNotJSON

class CurseForgeAPI:
    def __init__(self, api_key: str, use_cache: bool = True):
        self.api_key = api_key
        self.base_url = "https://api.curseforge.com/"
        self.use_cache = use_cache
        if self.use_cache:
            self.cache_obj = Cache()
    
    def fetch_raw(self, path: str):
        url = urljoin(self.base_url, path)
        response = get(url, headers={"x-api-key": self.api_key})
        try:
            return response.json()
        except JSONDecodeError as e:
            raise CurseResponseIsNotJSON from e
        except RequestException as e:
            raise CurseForgeError from e

    def fetch(self, path: str):
        if self.use_cache:
            if path in self.cache_obj:
                return self.cache_obj[path]
            else:
                data = self.fetch_raw(path)
                self.cache_obj[path] = data
                return data
        else:
            return self.fetch_raw(path)