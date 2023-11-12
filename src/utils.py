import datetime as dt
from dateutil import tz
from uuid import uuid4


def get_datetime(timezone="Europe/Paris") -> dt.datetime:
    """Get current datetime for timezone."""
    return dt.datetime.now(tz=tz.gettz(timezone))


def get_date() -> dt.date:
    """Get current date."""
    return get_datetime().date()


def generate_uuid() -> str:
    """Generate uuid as str.
    aaa_bbb_ccc_ddd."""
    return uuid4()