from pytz import timezone
from datetime import datetime, timedelta


time_zone = timezone('Asia/Singapore')

def get_current_datetime():
    current_datetime = datetime.now(time_zone)
    return current_datetime


def hours_between(d1, d2):
    '''
    Returns number of hours between two datetime.datetime objects
    Return type: int
    '''
    return int(abs((d2 - d1)).total_seconds()/3600)


def minutes_between(d1, d2):
    '''
    Returns number of hours between two datetime.datetime objects
    Return type: int
    '''
    return int(abs((d2 - d1)).total_seconds()/60)