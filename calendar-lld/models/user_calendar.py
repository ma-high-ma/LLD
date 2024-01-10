class UserCalendar:
    """
    Based on user_role, the user will have permissions over the calendar
    The creator of the calendar will be 'owner'
    When a calendar has been shared with a user, the role will be 'viewer'
    """
    def __init__(self, id, user_id, calendar_id, user_role="owner"):
        self.id = id
        self.user_id = user_id
        self.calendar_id = calendar_id
        self.user_role = user_role
