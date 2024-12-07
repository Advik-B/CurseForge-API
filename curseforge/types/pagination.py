from dataclasses import dataclass

@dataclass
class CursePagination:
    index: int
    pageSize: int
    resultCount: int
    totalCount: int

    @staticmethod
    def from_dict(data: dict):
        return CursePagination(
            index=data["index"],
            pageSize=data["pageSize"],
            resultCount=data["resultCount"],
            totalCount=data["totalCount"]
        )