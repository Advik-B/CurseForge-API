from requests import get
from dataclasses import dataclass

BASE_URL = "https://api.curseforge.com"


@dataclass()
class CurseClient:
    api_key: str

    def fetch(self, url: str):
        return get(
            BASE_URL + url,
            headers={
                "X-API-Key": self.api_key,
                "Accept": "application/json"
            }
        )
