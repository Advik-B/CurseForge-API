from dataclasses import dataclass

@dataclass
class CurseModAuthor:
    id: int
    name: str
    url: str

    @staticmethod
    def from_dict(d: dict):
        return CurseModAuthor(
            id=d.get('id'),
            name=d.get('name'),
            url=d.get('url')
        )