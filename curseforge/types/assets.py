from dataclasses import dataclass

@dataclass
class CurseAssets:
    iconUrl: str
    tileUrl: str
    coverUrl: str

    @staticmethod
    def from_dict(data: dict):
        return CurseAssets(
            iconUrl=data["iconUrl"],
            tileUrl=data["tileUrl"],
            coverUrl=data["coverUrl"]
        )