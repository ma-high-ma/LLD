from exceptions import UserNotFound
from models.user import User


class UserDao:
    UserMap = {}

    def create(self, id, name, email, password):
        user = User(id, name, email, password)
        self.UserMap[user.id] = user
        return user

    def get_by_id(self, id):
        try:
            return self.UserMap[id]
        except KeyError:
            raise UserNotFound(id=id)
