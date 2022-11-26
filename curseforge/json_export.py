from json import dump, load

from .classes import *
import codecs


def export_json(curse_obj: CurseObject) -> dict:
    json = {}
    for key, value in curse_obj.__dict__.items():
        if isinstance(value, CurseObject):
            json[key] = export_json(value)
        elif isinstance(value, (list, tuple)):
            json[key] = []
            for item in value:
                if isinstance(item, CurseObject):
                    json[key].append(export_json(item))
                else:
                    json[key].append(item)
        else:
            json[key] = value
    return json


def export_json_to_file(curse_obj: CurseObject, file: str):
    with codecs.open(file, "w", "utf-8") as f:
        dump(export_json(curse_obj), f, indent=4, ensure_ascii=False)
