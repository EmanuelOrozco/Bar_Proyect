from models.User import User


class LoginManager:
    def __init__(self):
        self.users: list[User] = []

    def validate(self, name: str, password: str):
        for user in self.users:
            if (user.name == name) and (user.password == password):
                return True
        return False
