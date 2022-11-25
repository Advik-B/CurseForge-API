from dataclasses import dataclass

@dataclass
class CurseGame:
    id: int
    name: str
    slug: str
    url: str
    assets: dict
    status: int
    api_status: int
    date_modified: str
