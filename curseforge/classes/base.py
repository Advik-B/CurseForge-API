from dataclasses import dataclass
from ..json_export import export_json


@dataclass
class CurseObject:
    def to_json(self): return export_json(self)