from dataclasses import dataclass

@dataclass
class Image:
    id: int
    modId: int
    title: str
    description: str
    thumbnail_url: str
    url: str

