from dataclasses import dataclass
from .json_export import export_json, export_dict

@dataclass
class CurseObject:
    def to_dict(self):
        return export_dict(self)

    def to_json(self):
        return export_json(self)
