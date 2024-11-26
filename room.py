# room.py
# id:202444001
# name: 유승원

import datetime as dt

time_format = "%Y-%m-%d %H:%M:%S"

class Room1:
    def __init__(self, num, start_time : dt.datetime, stop_time : dt.datetime = None):
        self.num = num
        self.start_time = start_time
        self.stop_time = stop_time 

    def diff_seconds(self):
        if self.stop_time == None or self.stop_time == "":
            temp_time = dt.datetime.now()
        else:
            temp_time = self.stop_time
        return (temp_time - self.start_time).total_seconds()
