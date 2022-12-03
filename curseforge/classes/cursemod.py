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

    @staticmethod
    def from_dict(data: dict):
        """
        Returns a CurseMod instance from a dict
        """

        return CurseMod(
            id=data.get("id"),
            game_id=data.get("gameId"),
            name=data.get("name"),
            slug=data.get("slug"),
            links=CurseModLinks(
                website_url=data.get("links").get("websiteUrl"),
                wiki_url=data.get("links").get("wikiUrl"),
                issue_tracker_url=data.get("links").get("issueTrackerUrl"),
                source_code_url=data.get("links").get("sourceCodeUrl")
            ),
            summary=data.get("summary"),
            status=data.get("status"),
            download_count=data.get("downloadCount"),
            is_featured=data.get("isFeatured"),
            primary_category_id=data.get("primaryCategoryId"),
            categories=tuple(CurseCategory.from_dict(category) for category in data.get("categories")),
            class_id=data.get("classId"),
            authors=tuple(CurseModAuthor(
                id=author.get("id"),
                name=author.get("name"),
                url=author.get("url")
            ) for author in data.get("authors")),
            logo=CurseModLogo(
                id=data.get("logo").get("id"),
                url=data.get("logo").get("url"),
                thumbnail_url=data.get("logo").get("thumbnailUrl")
            ),
            screenshots=tuple(CurseScreenShot(
                id=screenshot.get("id"),
                url=screenshot.get("url"),
                thumbnail_url=screenshot.get("thumbnailUrl")
            ) for screenshot in data.get("screenshots")),
            mainFile_id=data.get("mainFileId"),
            latestFiles=tuple(CurseModFile(
                id=file.get("id"),
                game_id=file.get("gameId"),
                mod_id=file.get("modId"),
                isAvailable=file.get("isAvailable"),
                display_name=file.get("displayName"),
                file_name=file.get("fileName"),
                release_type=file.get("releaseType"),
                file_status=file.get("fileStatus"),
                hashes=tuple(CurseHash(
                    hash=file.get("hashes").get("hash"),
                    type=file.get("hashes").get("type")
                ) for file in data.get("latestFiles")),
                file_date=file.get("fileDate"),
                file_length=file.get("fileLength"),
                download_count=file.get("downloadCount"),
                download_url=file.get("downloadUrl"),
                game_versions=file.get("gameVersions"),
                sortable_game_version=tuple(CurseSortableGameVersion(
                    game_version_name=version.get("gameVersionName"),
                    game_version_padded=version.get("gameVersionPadded"),
                    game_version=version.get("gameVersion"),
                    game_version_release_date=version.get("gameVersionReleaseDate"),
                    game_version_type_id=version.get("gameVersionTypeId")
                ) for version in data.get("sortableGameVersion")),
                dependencies=tuple(CurseDependency(
                    mod_id=dependency.get("modId"),
                    relation_type=dependency.get("relationType")
                ) for dependency in data.get("dependencies")),

                expose_as_alternate=file.get("exposeAsAlternate"),
                parent_project_file_id=file.get("parentProjectFileId"),
                altername_file_id=file.get("alternameFileId"),
                is_server_pack=file.get("isServerPack"),
                server_pack_file_id=file.get("serverPackFileId"),
                file_finger_print=file.get("fileFingerPrint"),
                modules=tuple(CurseModule(
                    name=module.get("name"),
                    fingerprint=module.get("fingerprint")
                ) for module in data.get("modules"))
            ) for file in data.get("latestFiles")),
            latestFilesIndexes=tuple(CurseFileIndex(
                game_version=ver.get("gameVersion"),
                file_id=ver.get("fileId"),
                release_type=ver.get("releaseType"),
                game_version_type_id=ver.get("gameVersionTypeId"),
                modloader=ver.get("modloader")
                for ver in data.get("latestFilesIndexes")
            ),
            data_created=data.get("dataCreated"),
            data_modified=data.get("dataModified"),
            data_released=data.get("dataReleased"),
            allow_mod_distribution=data.get("allowModDistribution"),
            game_popularity_rank=data.get("gamePopularityRank"),
            is_available=data.get("isAvailable"),
            thumbs_up_count=data.get("thumbsUpCount")
        )

