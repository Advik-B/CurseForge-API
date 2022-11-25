from requests import get
from dataclasses import dataclass

BASE_URL = "https://api.curseforge.com"


@dataclass()
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
        ).json().get("data")
