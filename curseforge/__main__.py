from base64 import b64decode
from .util import parse_manifest_file
from .base import CurseClient
from .classes import CurseManifest
from argparse import ArgumentParser
from . import VERSION

from .classes import CurseGame

# I know that the API key is public, but it's not like it's going to be used for anything
# I'm not going to be using this API key for anything else, so it's fine
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode(
    "utf-8")


parser = ArgumentParser(description="A no-compromises wrapper for the CurseForge API", prog="curseforge")
parser.add_argument("-v", "--version", action="version", version=VERSION)
parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
parser.add_argument("-k", "--api-key", help="The API key to use for the API", default="builtin")
parser.add_argument("-c", "--cache", action="store_true", help="Enable caching for the API", default=True)
parser.add_argument_group("Commands")
subparsers = parser.add_subparsers(dest="command")
subparsers.required = True
# CMPDL
cmpdl_parser = subparsers.add_parser("cmpdl", help="Download a modpack from CurseForge")
cmpdl_parser.add_argument("-s", "--source", required=True, help="The source of the modpack")
cmpdl_parser.add_argument("-o", "--output", required=True, help="The output directory")
cmpdl_parser.add_argument("-K", "--keep", action="store_true", help="Keep the downloaded config files")

# Cache Dignostics Tool
cache_parser = subparsers.add_parser("cache", help="Run the cache diagnostics tool")
cache_parser.add_argument("-i", "--indent", action="store_true", help="Indent the JSON output")
cache_parser.add_argument("-k", "--key", help="The key to probe")
cache_parser.add_argument("-s", "--search", help="Search for a key")
cache_parser.add_argument("-d", "--delete", help="Delete a key")
cache_parser.add_argument("-c", "--clear", action="store_true", help="Clear the cache")
cache_parser.add_argument("-l", "--list", action="store_true", help="List all keys in the cache")
cache_parser.add_argument("-r", "--raw", action="store_true", help="Print the raw data")
cache_parser.add_argument("-o", "--output", help="Output the cache to a file in JSON format")
cache_parser.add_argument("-O", "--output-raw", help="Output the cache to a file in raw format")

# fetch command
fetch_parser = subparsers.add_parser("fetch", help="Fetch data from the CurseForge API")
# curseforge fetch /games/432
fetch_parser.add_argument("url", help="The URL to fetch")
fetch_parser.add_argument("-m", "--method", help="The HTTP method to use", default="GET")
fetch_parser.add_argument("-p", "--params", help="The parameters to pass to the API", default={})
fetch_parser.add_argument("-r", "--raw", action="store_true", help="Always use HTTP(s) instead of the cache")

args = parser.parse_args()
print(args)