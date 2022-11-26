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


class SortableGameVersion(CurseObject):
    game_version_name: str
    game_version_padded: str
    game_version: str
    game_version_release_date: str
    game_version_type_id: int


class Dependency(CurseObject):
    mod_id: int
    relation_type: int

class Module(CurseObject):
    name: str
    fingerprint: int

class FileIndex(CurseObject):
    game_version: str
    file_id: int
    file_name: str
    release_type: int
    game_version_type_id: int
    mod_loader: int

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
    game_versions: tuple[str]
    sortable_game_version: tuple[SortableGameVersion]
    dependencies: tuple[Dependency]
    expose_as_alternate: bool
    parent_project_file_id: int
    altername_file_id: int
    is_server_pack: bool
    server_pack_file_id: int
    file_finger_print: str
    modules: tuple[Module]





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
    latestFilesIndexes: tuple[FileIndex]
    data_created: str
    data_modified: str
    data_released: str
    allow_mod_distribution: bool
    game_popularity_rank: int
    is_available: bool
    thumbs_up_count: int

