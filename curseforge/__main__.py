from base64 import b64decode
from .base import CurseClient
from .classes import CurseGame
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=True)

# minecraft: CurseGame
JEI_file = client.get_mod_file(400012, 4083676)
print(JEI_file.download_url) # https://edge.forgecdn.net/files/4083/676/ExNihiloSequentia-1.18.2-20221113-044349.jar