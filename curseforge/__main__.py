from base64 import b64decode
from .base import CurseClient
from .classes import CurseGame
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=True)

mod_file_list = {
  "minecraft": {
    "version": "1.18.2",
    "modLoaders": [
      {
        "id": "forge-40.1.84",
        "primary": True
      }
    ]
  },
  "manifestType": "minecraftModpack",
  "manifestVersion": 1,
  "name": "Sample CMPDL Testing modpack",
  "version": "6.9.4.2.0",
  "author": "Advik",
  "files": [
    {
      "projectID": 319596,
      "fileID": 3457597,
      "required": True
    },
    {
      "projectID": 400012,
      "fileID": 4083676,
      "required": True
    },
    {
      "projectID": 314906,
      "fileID": 3466965,
      "required": True
    },
    {
      "projectID": 552574,
      "fileID": 4019567,
      "required": True
    },
    {
      "projectID": 419699,
      "fileID": 3442690,
      "required": True
    }
  ],
  "overrides": "overrides"
}

# minecraft: CurseGame
# file = client.get_mod_file(400012, 4083676)
# print(file.download_url) # https://edge.forgecdn.net/files/4083/676/ExNihiloSequentia-1.18.2-20221113-044349.jar

mods = mod_file_list["files"]

for mod in mods:
    file = client.get_mod_file(mod["projectID"], mod["fileID"])
    print(file.download_url)