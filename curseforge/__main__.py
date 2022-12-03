from base64 import b64decode
from .base import CurseClient
from .classes import CurseGame
from pprint import pprint
from requests import get
from .export import export_json, export_dict
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=True)

# minecraft: CurseGame

ID_minecraft: int = 432
minecraft: CurseGame = client.game(ID_minecraft)
pprint(minecraft)
pprint(export_dict(minecraft))

# client.clean_cache()