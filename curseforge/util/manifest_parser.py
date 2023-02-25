from json import loads
from ..classes.manifest import CurseManifest
from codecs import open


def parse_manifest(manifest: str) -> dict:
    """Parses a manifest file and returns a dict"""
    with open(manifest, "r", "utf-8") as file:
        return CurseManifest.from_dict(loads(file.read()))
