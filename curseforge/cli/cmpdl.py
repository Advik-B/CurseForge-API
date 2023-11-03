from ..base import CurseClient
import re

CURSEFORGE_URL_REGEX = re.compile(r"https?://(?:www\.)?curseforge\.com/minecraft/modpacks/([a-zA-Z0-9\-_]+)")

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
            self.dprintf("Modpack ID:", modpack_id)
            if modpack_id.isalpha():
                self.dprintf("Modpack ID is alpha, assuming slug")
                mpack = self.client.addon_from_slug(modpack_id)
                print(mpack)
            self.dprintf("Modpack:", mpack)
