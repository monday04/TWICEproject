# import countdowntimer
import pytz
import datetime as datetime2
from datetime import datetime, timedelta


class MusicShow(object):
    """
    Class to represent a Music Show. This will automatically assume as today's date as reference
    Attributes:
        show_name(str): name of the music show
        tracking_date: varies by music show
    """
    def __init__(self, show_name):
        self.show_name = show_name
        self.tracking_date = 0
        dday = 0

        # --------------- calculate tracking time by music show--------------- #
        if self.show_name in ["MUC", "INK"]:
            print(f"{show_name}: tracking from monday to monday...")
            dday = 9

        if self.show_name in ["SCP", "MCD", "MUB"]:
            print(f"{show_name}: tracking from monday to sunday...")
            dday = 8

        # ---------- get current time in south korea ------------------- #
        now_kor = datetime2.datetime.now((pytz.timezone('Asia/Seoul')))
        kdate = now_kor.today()
        kday = now_kor.weekday()

        # --------------- calculate date of day1 tracking period --------------- #
        self.start_day = kdate - timedelta(kday)
        print(f"\tStart tracking day: {self.start_day} --- KST", )
        self.end_day = kdate + timedelta(dday-kday)
        print(f"\tEnd tracking day: {self.end_day.date()} 00:00:00--- KST\n")

        # --------------- convert end tracking day to system time --------------- #
        kr_tz = pytz.timezone('Asia/Seoul')
        dt = datetime(self.end_day.year, self.end_day.month, self.end_day.day, 0, 0, 0)
        self.end_day_local = kr_tz.localize(dt).astimezone()
        print(self.end_day_local)


# inkigayo = MusicShow("INK")
# music_core = MusicShow("MUC")
# sho_chmp = MusicShow("SCP")
# music_bank = MusicShow("MUB")
#
# t = countdowntimer.CountdownTimer(inkigayo.end_day_local).countdowntimer()
# print(t)