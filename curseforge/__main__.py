from base64 import b64decode
from pprint import pprint
from .base import CurseClient
from .classes import CurseGame
from .export import export_json
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=True)

# minecraft: CurseGame
JEI_file = client.get_mod_file(238222, 4087658)
pprint(JEI_file)
# client.clean_cache()