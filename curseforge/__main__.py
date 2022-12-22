from base64 import b64decode
from dataclasses import dataclass

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

def Print(*text, end: str = "\n\r", sep: str = " ", flush: bool = False):
    for i in text:
        stdout.write(str(i))
        stdout.write(sep)
    stdout.write(end)
    if flush:
        stdout.flush()



for mod in mod_file_list:
    file = client.get_mod_file(mod["projectID"], mod["fileID"])
    Print(file.download_url)
    # for key in dir(file):
    #     Print("="*80)
    #     Print(f"Key: {key}" + " | Value:", eval(f"file.{key}", globals(), locals()))
    # Print("="*80)
