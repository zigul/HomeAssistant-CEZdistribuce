import requests
import datetime

BASE_URL = "https://www.cezdistribuce.cz/edee/content/sysutf/ds3/data/hdo_data.json"

def getRequestUrl(region, code):
    return BASE_URL + "?&code=" + code + "&"+ region +"=1"

def timeInRange(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def parseTime(date_time_str):
    if(not date_time_str):
        return datetime.time(0,0)
    else:
        return datetime.datetime.strptime(date_time_str, '%H:%M').time()

def parseDate(date_time_str):
    return datetime.datetime.strptime(date_time_str,'%Y-%m-%d %H:%M:%S.%f')

def isHdo(jsonCalendar):
    now = datetime.datetime.now()
    if(now.weekday()<5):
        days = jsonCalendar[0]
    else:
        days = jsonCalendar[1]

    actualTime = now.time()
    hdo = False
    for i in range(1,11):
        startTime = parseTime(days["casZap" + str(i)])
        endTime = parseTime(days["casVyp" + str(i)])
        hdo = hdo or timeInRange(startTime, endTime, actualTime)
    return hdo