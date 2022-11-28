from json import dumps
from .classes.base import CurseObject

def export_dict(obj: CurseObject):
    for key, value in obj.__dict__.items():
        if isinstance(value, CurseObject):
            obj.__dict__[key] = value.__dict__
    return obj.__dict__


def export_json(obj: CurseObject, indent: int = 4):
    for key, value in obj.__dict__.items():
        if isinstance(value, CurseObject):
            obj.__dict__[key] = value.__dict__
    return dumps(obj.__dict__, indent=indent)
