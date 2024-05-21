from ..base import CurseClient
import re

CURSEFORGE_URL_REGEX = re.compile(r"https?://(?:www\.)?curseforge\.com/minecraft/modpacks/([a-zA-Z0-9\-_]+)")
CURSEFORGE_URL_FILES = re.compile(r"https?://(?:www\.)?curseforge\.com/minecraft/modpacks/[a-zA-Z0-9\-_]+/files/([0-9]+)")


class Program():
    def __init__(
            self,
            src: str,
            out: str,
            keep: bool,
            client: "CurseClient",
            printf: callable,
            dprintf: callable,
    ) -> None:
        self.src = src
        self.out = out
        self.keep = keep
        self.client = client
        self.SOURCE_MODE: str = "unknown"
        self.printf: print = printf
        self.dprintf: print = dprintf
        self.parse_source()

    def parse_source(self) -> None:
        if CURSEFORGE_URL_REGEX.match(self.src):
            self.SOURCE_MODE = "curseforge"
            self.dprintf("Detected CurseForge URL")

        elif self.src.startswith("http"):
            self.SOURCE_MODE = "url"
            self.dprintf("Detected URL")

        elif self.src.startswith("file://"):
            self.SOURCE_MODE = "file"
            self.dprintf("Detected file path")
            self.src = self.src[7:]

        else:
            self.SOURCE_MODE = "file"
            self.dprintf("Assuming file path for source: ", self.src)


    def run(self) -> None:
        if self.SOURCE_MODE == "curseforge":
            self.dprintf("Downloading modpack from CurseForge")
            modpack_id = CURSEFORGE_URL_REGEX.match(self.src).group(1)
            file_iead = CURSEFORGE_URL_FILES.match(self.src).group(1)
            self.dprintf("Modpack ID:", modpack_id)
            mpack_id: int
            file_id: int
            if modpack_id.isalpha():
                self.dprintf("Modpack ID is a slug, converting to ID")
                mpack_id = self.client.addon_from_slug(modpack_id).id

            else:
                mpack_id = int(modpack_id)

            self.dprintf("Modpack ID:", mpack_id)
            self.dprintf("Fetching modpack data")
            if file_iead is not None:
                file_id = int(file_iead)
            else:
                file_id = self.client.addon(mpack_id).latestFiles[0].id

            self.dprintf("File ID:", file_id)
            self.dprintf("Downloading modpack")
            self.download_modpack(mpack_id, file_id)

        elif self.SOURCE_MODE == "url":
            self.dprintf("Downloading modpack from URL")
            self.dprintf("Fetching URL")
            self.dprintf("Downloading modpack")
            self.download_modpack_from_url(self.src)

    def download_modpack(self, modpack_id: int, file_id: int):
