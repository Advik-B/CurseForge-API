import os
from curseforge import CurseForgeAPI
from curseforge.types import CurseGame


API = CurseForgeAPI(os.getenv("CURSEFORGE_TOKEN"), use_cache=False)

games = CurseGame.s(API) # The .s() method for any type in curseforge that will list all of *it* from the API

for game in games:
    print(game.id, game.name)
