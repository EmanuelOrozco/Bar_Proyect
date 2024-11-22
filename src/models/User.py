from abc import ABC

class User(ABC):
    def __init__(self, name:str , password: str) -> None:
        self.name: str = name
        self.password : str = password