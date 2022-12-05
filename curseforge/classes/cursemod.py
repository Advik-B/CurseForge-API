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
@dataclass
class CurseModLogo(CurseImage): pass

@dataclass
class CurseScreenShot(CurseImage): pass

@dataclass
class CurseSortableGameVersion(CurseObject):
    game_version_name: str
    game_version_padded: str
    game_version: str
    game_version_release_date: str
    game_version_type_id: int

    @staticmethod
    def from_dict(data: dict):
        return CurseSortableGameVersion(
            game_version_name=data.get("gameVersionName"),
            game_version_padded=data.get("gameVersionPadded"),
            game_version=data.get("gameVersion"),
            game_version_release_date=data.get("gameVersionReleaseDate"),
            game_version_type_id=data.get("gameVersionTypeId")
        )

@dataclass
class CurseDependency(CurseObject):
    mod_id: int
    relation_type: int

    @staticmethod
    def from_dict(data: dict):
        return CurseDependency(
            mod_id=data.get("mod_id"),
            relation_type=data.get("relation_type")
        )


@dataclass
class CurseModule(CurseObject):
    name: str
    fingerprint: int

    @staticmethod
    def from_dict(data: dict):
        return CurseModule(
            name=data.get("name"),
            fingerprint=data.get("fingerprint")
        )

@dataclass
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

    @staticmethod
    def from_dict(data: dict):
        return CurseModFile(
            id=data.get("id"),
            game_id=data.get("gameId"),
            mod_id=data.get("modId"),
            isAvailable=data.get("isAvailable"),
            display_name=data.get("displayName"),
            file_name=data.get("fileName"),
            release_type=data.get("releaseType"),
            file_status=data.get("fileStatus"),
            hashes=tuple(CurseHash.from_dict(hash_) for hash_ in data.get("hashes")), # type: ignore
            file_date=data.get("fileDate"),
            file_length=data.get("fileLength"),
            download_count=data.get("downloadCount"),
            download_url=data.get("downloadUrl"),
            game_versions=tuple(data.get("gameVersions")),
            sortable_game_version=tuple(CurseSortableGameVersion.from_dict(version) for version in data.get("sortableGameVersions")),
            dependencies=tuple(CurseDependency.from_dict(dependency) for dependency in data.get("dependencies")),
            expose_as_alternate=data.get("exposeAsAlternate"),
            parent_project_file_id=data.get("parentProjectFileId"),
            altername_file_id=data.get("alternameFileId"),
            is_server_pack=data.get("isServerPack"),
            server_pack_file_id=data.get("serverPackFileId"),
            file_finger_print=data.get("fileFingerPrint"),
            modules=tuple(CurseModule.from_dict(module_) for module_ in data.get("modules")),
        )


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

    @staticmethod
    def from_dict(data: dict):
        """
        Returns a CurseMod instance from a dict
        """

        return

