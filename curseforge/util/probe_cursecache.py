from diskcache import Cache
from json import dumps
cache = Cache('cache/curseforge')

BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

INDENT = 0

for key in cache:
    print(BOLD + GREEN + key + RESET)

    if INDENT > 0:
        strdump = dumps(cache[key], indent=INDENT)
    else:
        strdump = dumps(cache[key])
    print(YELLOW + strdump + RESET)
    print()
