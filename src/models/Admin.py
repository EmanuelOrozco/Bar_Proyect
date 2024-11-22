from User import User

class Admin(User):
    id_general: int = 1
    
    def __init__(self, name: str, password: str):
        super().__init__(name, password)

        self.id_admin: int = self.id_general
        self.id_general += 1
