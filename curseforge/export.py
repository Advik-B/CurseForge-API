from json import dumps
from .classes.base import CurseObject

def export_dict(obj: CurseObject):
    for key, value in obj.__dict__.items():
        if type(obj) == CurseObject:
            obj.__dict__[key] = value.__dict__
    return obj.__dict__


def export_json(obj: CurseObject, indent: int = 4):
    dickt = export_dict(obj)
    return dumps(dickt, indent=indent)
