from json import dumps

def export_json(curse_obj: object) -> dict:
    """
    This function should not be used directly. Use export_dict
    """
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


def export_json(curse_obj: object) -> str:
    """
    This function should not be used directly. Use export_json_to_file
    """
    return dumps(export_json(curse_obj))
