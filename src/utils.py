import datetime as dt
from dateutil import tz


def get_datetime(timezone="Europe/Paris"):
    return dt.datetime.now(tz=tz.gettz(timezone))


def get_date():
    return get_datetime().date()
