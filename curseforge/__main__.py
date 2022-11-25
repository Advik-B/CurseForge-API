from base64 import b64decode
from .base import CurseClient

API_KEY: str = b64decode("JDJhJDEwJFhkNkhYT3dweFI1UTIvWGpyZjBkUC5hSDFaRDE5T3pRZC9mVnVNLk94QXJJL01DTlZtNHZh").decode("utf-8")

client = CurseClient(API_KEY)
print(client.get("/v1/games").json())