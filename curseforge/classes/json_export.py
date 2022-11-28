from json import dumps


def export_dict(curse_obj: object) -> dict:
    """
    This function should not be used directly. Use export_dict
    """
    json = {}
    for key, value in curse_obj.__dict__.items():
        if key.startswith("_"):
            continue
        if isinstance(value, list):
            json[key] = [export_dict(i) for i in value]
        elif isinstance(value, object):
            json[key] = export_dict(value)
        else:
            json[key] = value

    return json



def export_json(curse_obj: object) -> str:
    """
    This function should not be used directly. Use export_json_to_file
    """
    return dumps(export_json(curse_obj))
