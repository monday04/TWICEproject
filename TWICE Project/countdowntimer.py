import time
from datetime import datetime


class CountdownTimer:

    def __init__(self, end_day_local):
        self.end_day_local = end_day_local
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # --------------- countdown timer procedure --------------- #
    def countdowntimer(self):
        while True:
            now_date = datetime.now()
            count = int((self.end_day_local.replace(tzinfo=None) - now_date).total_seconds())
            self.days = count//86400
            self.hours = (count-self.days*86400)//3600
            self.minutes = (count-self.days*86400-self.hours*3600)//60
            self.seconds = count-self.days*86400-self.hours*3600-self.minutes*60

            # print("{} : {} : {} : {}".
            #       format(self.days, self.hours, self.minutes, self.seconds))

            self.t = str("{} : {} : {} : {}".format(self.days, self.hours, self.minutes, self.seconds))
            return self.t

            time.sleep(1)
