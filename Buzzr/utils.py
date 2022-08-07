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



postal_district_mapping = {
    '01': 1,
    '02': 1,
    '03': 1,
    '04': 1,
    '05': 1,
    '06': 1,
    '07': 2,
    '08': 2,
    '09': 4,
    '10': 4,
    '11': 5,
    '12': 5,
    '13': 5,
    '14': 3,
    '15': 3,
    '16': 3,
    '17': 6,
    '18': 7,
    '19': 7,
    '20': 8,
    '21': 8,
    '22': 9,
    '23': 9,
    '24': 10,
    '25': 10,
    '26': 10,
    '27': 10,
    '28': 11,
    '29': 11,
    '30': 11,
    '31': 12,
    '32': 12,
    '33': 12,
    '34': 13,
    '35': 13,
    '36': 13,
    '37': 13,
    '38': 14,
    '39': 14,
    '40': 14,
    '41': 14,
    '42': 15,
    '43': 15,
    '44': 15,
    '45': 15,
    '46': 16,
    '47': 16,
    '48': 16,
    '49': 17,
    '50': 17,
    '81': 17,
    '51': 18,
    '52': 18,
    '53': 19,
    '54': 19,
    '55': 19,
    '82': 19,
    '56': 20,
    '57': 20,
    '58': 21,
    '59': 21,
    '60': 22,
    '61': 22,
    '62': 22,
    '63': 22,
    '64': 22,
    '65': 23,
    '66': 23,
    '67': 23,
    '68': 23,
    '69': 24,
    '70': 24,
    '71': 24,
    '72': 25,
    '73': 25,
    '75': 27,
    '76': 27,
    '77': 26,
    '78': 26,
    '79': 28,
    '80': 28
}

area_mapping = {
    5: "west",
    22: "west",
    23: "west",
    24: "north",
    25: "north",
    27: "north",
    19: "north-east",
    20: "north-east",
    28: "north-east",
    15: "east",
    16: "east",
    17: "east",
    18: "east",
    1: "central",
    2: "central",
    3: "central",
    4: "central",
    6: "central",
    7: "central",
    8: "central",
    9: "central",
    10: "central",
    11: "central",
    12: "central",
    13: "central",
    14: "central",
    21: "central",
    26: "central",
}