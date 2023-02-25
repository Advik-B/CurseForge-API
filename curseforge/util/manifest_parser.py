from json import loads
from ..classes.manifest import CurseManifest

def parse_manifest(manifest: str) -> dict:
    """Parses a manifest file and returns a dict"""
    return loads(manifest)