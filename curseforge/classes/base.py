from dataclasses import dataclass

@dataclass
class CurseObject:
    @property
    def json(self):
        for k, v in self.__dict__.items():
            self.__dict__[k] = v.json if isinstance(v, CurseObject) else v
        return self.__dict__
