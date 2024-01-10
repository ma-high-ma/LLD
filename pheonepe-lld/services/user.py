
from dao.user import UserDao
from exceptions import UserNotFound


class UserService:
    def create(self, id, name, email, password):
        # if not self.check_email(email):
        #     return
        return UserDao().create(id, name, email, password)

    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, email):
            return True
        else:
            print("Invalid email")
            return False

    def get_user_by_id(self, id):
        try:
            return UserDao().get_by_id(id)
        except UserNotFound as e:
            print("Error: ", str(e))
            return None