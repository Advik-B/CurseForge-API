from dataclasses import dataclass

@dataclass
class ModAuthor:
    id: int
    name: str
    url: str

    @staticmethod
    def from_dict(d: dict):
        return ModAuthor(
            id=d.get('id'),
            name=d.get('name'),
            url=d.get('url')
        )