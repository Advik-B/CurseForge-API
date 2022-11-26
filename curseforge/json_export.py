from json import dump, load

from .classes import *
from .base import CurseClient


def export_json(curse_obj: CurseObject) -> dict:
    json = {}
    for key, value in curse_obj.__dict__.items():
        if isinstance(value, CurseObject):
            json[key] = export_json(value)
        elif isinstance(value, list) or isinstance(value, tuple):
            json[key] = []
            for item in value:
                if isinstance(item, CurseObject):
                    json[key].append(export_json(item))
                else:
                    json[key].append(item)
        else:
            json[key] = value
    return json
