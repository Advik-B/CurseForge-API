from json import dump, load

from .classes import *
from .base import CurseClient
def export_json(curse_obj: CurseObject, file_name: str, indent: int = 4):
    json = {}
    for key, value in curse_obj.__dict__.items():
        if isinstance(value, CurseObject):
            json[key] = export_json(value, file_name)
        elif isinstance(value, list):
            json[key] = []
            for item in value:
                if isinstance(item, CurseObject):
                    json[key].append(export_json(item, file_name))
                else:
                    json[key].append(item)
        else:
            json[key] = value

    with open(f"{file_name}.json", "w") as f:
        dump(json, f, indent=indent)
