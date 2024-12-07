from dataclasses import dataclass

@dataclass
class CurseModAsset:
    id: int
    modId: int
    title: str
    description: str
    thumbnailUrl: str
    url: str

    @staticmethod
    def from_dict(d: dict):
        return CurseModAsset(
            id=d.get('id'),
            modId=d.get('modId'),
            title=d.get('title'),
            description=d.get('description'),
            thumbnailUrl=d.get('thumbnailUrl'),
            url=d.get('url')
        )