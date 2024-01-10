import datetime

from models.activity_log import ActivityLog


class ActivityLogService:
    ActivityLogMap = {}

    def create(self, todo_list_id, task_id, activity, user_id, type):
        created_at = datetime.datetime.now()
        activity_log = ActivityLog(todo_list_id, task_id, activity, created_at, user_id, type)
        date = created_at.date()
        self.__add_to_activity_log_map(activity_obj=activity_log, date=date, todo_list_id=todo_list_id)
        print(self.ActivityLogMap)
        return activity_log

    def get_logs(self, start_date, end_date, todo_list_id, print=False):
        logs = []
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            day_activity = self.ActivityLogMap.get(start_date)
            activity = day_activity.get(todo_list_id, [])
            logs += activity
            start_date += delta

        if print:
            self.print_logs(logs)
        return logs

    def __add_to_activity_log_map(self, activity_obj, date, todo_list_id):

        if not self.ActivityLogMap.get(date):
            self.ActivityLogMap[date] = {}
        if not self.ActivityLogMap[date].get(todo_list_id):
            self.ActivityLogMap[date][todo_list_id] = []
        self.ActivityLogMap[date][todo_list_id].append(activity_obj)

    def print_logs(self, logs):
        for l in logs:
            print(l.__dict__)
        print()

    def aggregate_by_type(self, todo_list_id, type, start_date, end_date):
        logs = self.get_logs(start_date, end_date, todo_list_id)
        count = 0
        for l in logs:
            if l.type == type:
                count += 1
        print("There were a total of ", count ," ", type)
        print()


