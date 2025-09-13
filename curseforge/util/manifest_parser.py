from json import loads
from ..classes.manifest import CurseManifest
from codecs import open


def parse_manifest_file(manifest: str) -> CurseManifest:
    """Parses a manifest file and returns a CurseManifest object"""
    with open(manifest, "r", "utf-8") as file:
        data = loads(file.read())
        return CurseManifest.from_dict(data)


def parse_manifest(manifest_data: dict) -> CurseManifest:
    """Parses manifest data from a dict and returns a CurseManifest object"""
    return CurseManifest.from_dict(manifest_data)
