from base64 import b64decode
from .base import CurseClient
from .classes import Game
from pprint import pprint
from requests import get
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=False)

# minecraft: Game

ID_minecraft: int = 432

minecraft = client.game(ID_minecraft)
print(minecraft.to_json())
print("Fetching minecraft")
response = get("https://api.curseforge.com/v1/games/432", headers={"X-API-Key": API_KEY, "Accept": "application/json"})
print(response.json())

# for game in client.games():
#     if game.name == "Minecraft":
#         minecraft = game
#         break
