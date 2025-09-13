# CurseForge API Wrapper

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[cfapi]: https://docs.curseforge.com/
[cfapi-docs]: https://docs.curseforge.com/
[not-working-cfapi]: https://github.com/Owen-Cochell/cursepy
[cmpdl]: https://github.com/Advik-B/CMPDL

This is a no-compromise CurseForge API wrapper for Python. It is a complete re-write of [cursepy][not-working-cfapi] with a focus on simplicity, speed, and ease of use.

This wrapper provides:
- **Simple and intuitive API** that follows Python conventions
- **Disk caching** for faster response times and reduced API calls
- **Direct API access** via the `fetch` method for advanced users
- **Data export** to DICT, JSON, or YAML formats
- **Manifest parsing** for CurseForge modpack files
- **Search functionality** for finding mods, games, and categories
- **Type hints** for better IDE support and code clarity

## Features

- ✅ Simple and easy to use
- ✅ Caches responses from the API to disk for faster response times
- ✅ Allows direct access to the API via the `fetch` method
- ✅ Allows exporting of the objects to DICT, JSON, or YAML
- ✅ Can directly parse a manifest file from a CurseForge modpack
- ✅ Search functionality for mods
- ✅ Comprehensive error handling
- ✅ HTTPS support for secure API communication

## Installation

```bash
pip install curseforge
```

## Quick Start

### Basic Usage

```python
from curseforge import CurseClient

# Initialize the client with your API key
client = CurseClient("YOUR-API-KEY", cache=True)

# Get information about Minecraft
minecraft = client.game(432)  # 432 is the ID of Minecraft
print(f"Game: {minecraft.name}")

# Get a specific mod (JourneyMap example)
journeymap = client.mod(32274)  # 32274 is the ID of JourneyMap
print(f"Mod: {journeymap.name}")
print(f"Downloads: {journeymap.download_count:,}")
print(f"Summary: {journeymap.summary}")

# Get latest files for the mod
for file in client.get_mod_files(32274):
    print(f"File: {file.display_name}")
    if file.download_url:
        print(f"Download: {file.download_url}")
```

### Searching for Mods

```python
# Search for mods in Minecraft
search_results = client.search_mods(
    game_id=432,  # Minecraft
    search_filter="journeymap",
    sort_field=6,  # Sort by total downloads
    page_size=10
)

for mod in search_results:
    print(f"{mod.name}: {mod.download_count:,} downloads")
```

### Working with Games and Categories

```python
# List all available games
games = client.games()
for game in games:
    print(f"Game: {game.name} (ID: {game.id})")

# Get categories for Minecraft
categories = client.categories(432)  # Minecraft ID
for category in categories:
    print(f"Category: {category.name}")
```

### Manifest Parsing

```python
# Parse a CurseForge modpack manifest
from curseforge.util.manifest_parser import parse_manifest

with open("manifest.json", "r") as f:
    manifest = parse_manifest(f.read())

print(f"Modpack: {manifest.name}")
print(f"Version: {manifest.version}")
print(f"Author: {manifest.author}")

# Get mod files from manifest
for file_manifest in manifest.files:
    mod_file = client.manifest_to_modfile(file_manifest)
    print(f"Mod file: {mod_file.display_name}")
```

### Advanced Usage

```python
# Direct API access
raw_data = client.fetch("games/432")  # Direct API call
print(raw_data)

# Custom caching
client = CurseClient(
    api_key="YOUR-API-KEY",
    cache=True,
    cache_dir="my_custom_cache"
)

# Export data to different formats
mod = client.mod(32274)
print(mod.json)  # Export as dictionary

# Clean up cache when done
client.clean_cache()
client.close_cache()
```

## API Key Setup

To use this wrapper, you need a CurseForge API key:

1. Go to [CurseForge Core API Documentation](https://docs.curseforge.com/)
2. Register for an API key
3. Use the API key in your application

**Important**: Never commit your API key to version control. Use environment variables:

```python
import os
from curseforge import CurseClient

api_key = os.getenv("CURSEFORGE_API_KEY")
client = CurseClient(api_key)
```

## Error Handling

```python
from curseforge import CurseClient

client = CurseClient("YOUR-API-KEY")

try:
    mod = client.mod(12345)
    print(f"Found mod: {mod.name}")
except Exception as e:
    print(f"Error fetching mod: {e}")
```

## Testing

Run the test suite:

```bash
python test_curseforge.py
```

The tests include unit tests that don't require an API key and integration tests that do.

## Rate Limiting

The CurseForge API has rate limits. This wrapper includes automatic caching to help reduce API calls. Always enable caching in production:

```python
client = CurseClient("YOUR-API-KEY", cache=True)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python test_curseforge.py`
4. Make your changes
5. Ensure tests pass
6. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE.txt).

## Changelog

### v1.6.0
- ✅ Completed CurseMod.from_dict() implementation
- ✅ Added search functionality
- ✅ Fixed HTTPS API endpoints
- ✅ Added comprehensive test suite
- ✅ Improved documentation and examples
- ✅ Added proper error handling
- ✅ Repository cleanup and better .gitignore

## Related Projects

- [CMPDL][cmpdl] - CurseForge Modpack Downloader that uses this API wrapper
