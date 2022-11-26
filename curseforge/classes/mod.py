from dataclasses import dataclass
from .image import Image
from .base import CurseObject

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


@dataclass
class Mod: pass
