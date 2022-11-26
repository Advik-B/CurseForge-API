from dataclasses import dataclass

@dataclass
class GameAssets:
    icon_url: str
    tile_url: str
    cover_url: str

@dataclass
class Game:
    id: int
    name: str
    slug: str
    url: str
    assets: GameAssets
    status: int
    api_status: int
    date_modified: str