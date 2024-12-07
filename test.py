import os
from curseforge import CurseForgeAPI
from curseforge.types import CurseGame


API = CurseForgeAPI(os.getenv("CURSEFORGE_TOKEN"), use_cache=False)

games = CurseGame.s(API) # The .s() method for any type in curseforge that will list all of *it* from the API
minecraft = CurseGame.from_id(432, API) # The .from_id() method for any type in curseforge that will fetch a specific one from the API
