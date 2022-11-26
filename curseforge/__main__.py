from base64 import b64decode
from .base import CurseClient
from json import dump
from pprint import pprint
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=False)

# minecraft = client.game(432)

pprint(client.fetch("game/432"))