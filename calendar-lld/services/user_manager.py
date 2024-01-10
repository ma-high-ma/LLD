from models.user import User
from services.calendar_manager import CalendarManagerService


class UserManagerService:

    """
    User -> Calendar -> Day -> Events

    """
    userMap = {}

    def create_user(self, id, name):
        user = User(id=id, name=name)
        self.userMap[user.id] = user
        return user