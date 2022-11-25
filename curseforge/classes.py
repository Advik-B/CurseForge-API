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


@dataclass
class Category:
    id: int
    game_id: int
    name: str
    slug: str
    url: str
    icon_url: str
    date_modified: str
    is_Class: bool
    class_id: int
    parentCategory_id: int
    displayIndex: int


@dataclass
class ModAuthor:
    id: int
    name: str
    url: str

@dataclass
class ModLinks:
    website_url: str
    wiki_url: str
    issue_tracker_url: str
    source_code_url: str


@dataclass
class Image:
    id: int
    modId: int
    title: str
    description: str
    thumbnail_url: str
    url: str

@dataclass
class Mod: pass