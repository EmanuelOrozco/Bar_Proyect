class Admin:
    id_general: int = 1
    
    def __init__(self, name: str, password: str):
        self.name: str = name
        self.password: str = password

        self.id_admin: int = self.id_general
        self.id_general += 1
