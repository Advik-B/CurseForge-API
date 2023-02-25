from json import loads
from ..classes.manifest import CurseManifest
from codecs import open


def parse_manifest_file(manifest: str) -> dict:
    """Parses a manifest file and returns a dict"""
    with open(manifest, "r", "utf-8") as file:
        data = loads(file.read())
        return CurseManifest.from_dict(data)
