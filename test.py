import os
from curseforge import CurseForgeAPI
from curseforge.types import CurseGame


API = CurseForgeAPI(os.getenv("CURSEFORGE_TOKEN"), use_cache=False)

games = CurseGame.list(API)

for game in games:
    print(game.id, game.name)
