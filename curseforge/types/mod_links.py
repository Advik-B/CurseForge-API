from dataclasses import dataclass, field

@dataclass
class CurseModLinks:
    websiteUrl: str = field(default=None)
    wikiUrl: str = field(default=None)
    issuesUrl: str = field(default=None)
    sourceUrl: str = field(default=None)

    @staticmethod
    def from_dict(d: dict):
        return CurseModLinks(
            websiteUrl=d.get('websiteUrl'),
            wikiUrl=d.get('wikiUrl'),
            issuesUrl=d.get('issuesUrl'),
            sourceUrl=d.get('sourceUrl')
        )