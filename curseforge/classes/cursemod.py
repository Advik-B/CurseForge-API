from dataclasses import dataclass
from .curseimage import CurseImage
from .base import CurseObject
from .cursecategory import CurseCategory
from .hashe import CurseHash


@dataclass
class CurseModAuthor(CurseObject):
    id: int
    name: str
    url: str


@dataclass
class CurseModLinks(CurseObject):
    website_url: str
    wiki_url: str
    issue_tracker_url: str
    source_code_url: str


# CurseModLogo and CurseScreenShot are a subclass of CurseImage because they share the same attributes
class CurseModLogo(CurseImage): pass


class CurseScreenShot(CurseImage): pass


class CurseSortableGameVersion(CurseObject):
    game_version_name: str
    game_version_padded: str
    game_version: str
    game_version_release_date: str
    game_version_type_id: int


class CurseDependency(CurseObject):
    mod_id: int
    relation_type: int


class CurseModule(CurseObject):
    name: str
    fingerprint: int


class CurseFileIndex(CurseObject):
    game_version: str
    file_id: int
    file_name: str
    release_type: int
    game_version_type_id: int
    mod_loader: int


@dataclass
class CurseModFile(CurseObject):
    id: int
    game_id: int
    mod_id: int
    isAvailable: bool
    display_name: str
    file_name: str
    release_type: int
    file_status: int
    hashes: tuple[CurseHash]
    file_date: str
    file_length: int
    download_count: int
    download_url: str
    game_versions: tuple[str]
    sortable_game_version: tuple[CurseSortableGameVersion]
    dependencies: tuple[CurseDependency]
    expose_as_alternate: bool
    parent_project_file_id: int
    altername_file_id: int
    is_server_pack: bool
    server_pack_file_id: int
    file_finger_print: str
    modules: tuple[CurseModule]


@dataclass
class CurseMod(CurseObject):
    id: int
    game_id: int
    name: str
    slug: str
    links: CurseModLinks
    summary: str
    status: int
    download_count: int
    is_featured: bool
    primary_category_id: int
    categories: tuple[CurseCategory]
    class_id: int
    authors: tuple[CurseModAuthor]
    logo: CurseModLogo
    screenshots: tuple[CurseScreenShot]
    mainFile_id: int
    latestFiles: tuple[CurseModFile]
    latestFilesIndexes: tuple[CurseFileIndex]
    data_created: str
    data_modified: str
    data_released: str
    allow_mod_distribution: bool
    game_popularity_rank: int
    is_available: bool
    thumbs_up_count: int