from base64 import b64decode
from .base import CurseClient
from .classes import CurseGame
API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY, cache=True)

# minecraft: CurseGame

ID_minecraft: int = 432
minecraft: CurseGame = client.game(ID_minecraft)
print(minecraft.assets) # Minecraft

# client.clean_cache()