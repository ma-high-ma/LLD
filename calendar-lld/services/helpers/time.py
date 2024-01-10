class TimeHelper:
    def get_time_in_int(self, time_str):
        hours, minutes = time_str.split(":")
        hours, minutes = int(hours), int(minutes)
        return hours * 100 + minutes

    def get_time_in_str(self, time_int):
        hours, minutes = time_int//100, time_int%100
        return f"{hours}:{minutes}"

