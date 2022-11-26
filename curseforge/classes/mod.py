from dataclasses import dataclass
from .image import Image
from .base import CurseObject
from .category import Category
from .hashe import Hash


@dataclass
class ModAuthor(CurseObject):
    id: int
    name: str
    url: str


@dataclass
class ModLinks(CurseObject):
    website_url: str
    wiki_url: str
    issue_tracker_url: str
    source_code_url: str


# ModLogo and ScreenShot are a subclass of Image because they share the same attributes
class ModLogo(Image): pass


class ScreenShot(Image): pass


@dataclass
class ModFile(CurseObject):
    id: int
    game_id: int
    mod_id: int
    isAvailable: bool
    display_name: str
    file_name: str
    release_type: int
    file_status: int
    hashes: tuple[Hash]
    file_date: str
    file_length: int
    download_count: int
    download_url: str
    game_version: tuple[str]



@dataclass
class Mod(CurseObject):
    id: int
    game_id: int
    name: str
    slug: str
    links: ModLinks
    summary: str
    status: int
    download_count: int
    is_featured: bool
    primary_category_id: int
    categories: tuple[Category]
    class_id: int
    authors: tuple[ModAuthor]
    logo: ModLogo
    screenshots: tuple[ScreenShot]
    mainFile_id: int
    latestFiles: tuple[ModFile]

