# Curseforge API
[cfapi]: https://wow.curseforge.com/api
[cfapi-docs]: https://wow.curseforge.com/api/docs
[not-working-cfapi]: https://github.com/Owen-Cochell/cursepy
[cmpdl]: https://github.com/Advik-B/CMPDL

This is a no-compromise CurseForge API wrapper for python. It is a re-write of [cursepy][not-working-cfapi] which is maintained but not actively developed.
This project is a complete re-write of the original project, with a focus on simplicity and ease of use.

This project is still in development, and is not yet ready for production use.
It also speeds up the process by using disk caching, It will cache the response from the API and will only make a new request if the request is not cached.

This, of course can be disabled by setting the cache to False.

## Features
- Simple and easy to use
- Caches responses from the API to disk for faster response times
- Allows direct access to the API via the `fetch` method
- Allows exporting of the objects to DICT, JSON, or YAML

## Installation

```bash
pip install curseforge
```

## Usage

```python
from curseforge import CurseClient

client = CurseClient("API-KEY", cache=True)

minecraft = client.game(432) # 432 is the ID of Minecraft

# or we can list all the games
games = client.games()

for game in games:
    print(game.name)

# The search is up to the user to implement, this is just a wrapper

# We can also get the latest files for a project

JourneyMap = client.mod(2238) # 2238 is the ID of JourneyMap

for file in JourneyMap.files:
    print(file.name)
```

## TODO
- [x] Implement the export methods
- [x] Implement the cache
- [ ] Implement the fetch method
- [ ] Deal with the download URL being a null value

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
