from requests import get
from dataclasses import dataclass

BASE_URL = "https://api.curseforge.com"

@dataclass
class CurseClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get(self, url: str):
        return get(BASE_URL + url, headers={"X-API-Key": self.api_key, "Accept": "application/json"})
