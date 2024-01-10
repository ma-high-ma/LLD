from models.user import User


class UserService:
    UserMap = {}

    def create(self, id, name):
        user = User(id=id, name=name)
        self.UserMap[user.id] = user
        return user
