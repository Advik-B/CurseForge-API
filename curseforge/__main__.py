from base64 import b64decode
from .base import CurseClient
from sys import stdout

from .classes import CurseGame
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=True)

mod_file_list = [
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
]

# minecraft: CurseGame
# file = client.get_mod_file(400012, 4083676)
# print(file.download_url) # https://edge.forgecdn.net/files/4083/676/ExNihiloSequentia-1.18.2-20221113-044349.jar



for mod in mod_file_list:
    file = client.get_mod_file(mod["projectID"], mod["fileID"])
    print(file.download_url, flush=True, end="\n\r")