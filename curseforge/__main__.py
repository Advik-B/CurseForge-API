from base64 import b64decode
from .base import CurseClient
from .classes import Game
from pprint import pprint
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=False)

minecraft: Game

for game in client.games():
    if game.name == "Minecraft":
        minecraft = game
        break

pprint(minecraft)