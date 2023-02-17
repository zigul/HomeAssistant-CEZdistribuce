import requests
import datetime

try:
    # python 3.9+
    from zoneinfo import ZoneInfo
except ImportError:
    # python 3.6-3.8
    from backports.zoneinfo import ZoneInfo


BASE_URL = "https://www.cezdistribuce.cz/distHdo/adam/containers/"
CEZ_TIMEZONE = ZoneInfo("Europe/Prague")


def getCorrectRegionName(region):
    region = region.lower()
    for x in ["zapad", "sever", "stred", "vychod", "morava"]:
        if x in region:
            return x


def getRequestUrl(region, code):
    region = getCorrectRegionName(region)
    return BASE_URL + region + "?&code=" + code.upper()


def timeInRange(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def parseTime(date_time_str):
    if not date_time_str:
        return datetime.time(0, 0)
    else:
        return datetime.datetime.strptime(date_time_str, "%H:%M").time()

def dayCodeCZ(Day):
# return day code for strung Day in czech formating
    Day = Day.lower()   # convert to lower case
    Day = Day.strip()   # remove any leading or trailing spaces
    if Day == "po":
        Code = 0
    elif Day == "út":
        Code = 1
    elif Day == "st":
        Code = 2
    elif Day == "čt":
        Code = 3
    elif Day == "pá":
        Code = 4
    elif Day == "so":
        Code = 5
    elif Day == "ne":
        Code = 6
    else:
        Code = -1      
    return Code

def isDay(firstLastDay, weekDay):
# firtsLastDay is string in format lika 'Po - Pá' or 'So - Ne'
# weekDay is Code return by weekday() function 0-6 (0 = Monday .. 6 = Sunday)
# function return true if weekDay is within firtsLastday

    dayList = firstLastDay.split('-')
    firstDay = dayCodeCZ(dayList[0])
    if len(dayList)<=1:
        lastDay = firstDay
    else:
        lastDay = dayCodeCZ(dayList[1])
    # print("FirstDay = ",firstDay,"; LastDay = ",lastDay)
    if weekDay>=firstDay and weekDay<=lastDay:
        return True
    else:
        return False

def isHdo(jsonCalendar):
    """
    Find out if the HDO is enabled for the current timestamp
    :param jsonCalendar: JSON with calendar schedule from CEZ
    :param daytime: relevant time in "Europe/Prague" timezone to check if HDO is on or not
    :return: bool
    """
    daytime = datetime.datetime.now(tz=CEZ_TIMEZONE)
    # select Mon-Fri schedule or Sat-Sun schedule according to current date
    #if daytime.weekday() < 5:
    #    dayCalendar = jsonCalendar[0]
    #else:
    #    dayCalendar = jsonCalendar[1]
    checkedTime = daytime.time()
    hdo = False

    for dayCalendar in jsonCalendar:
        firstLastDay = dayCalendar["PLATNOST"]
        if isDay(firstLastDay,daytime.weekday()):
            # iterate over scheduled times in calendar schedule
            for i in range(1, 11):
                startTime = parseTime(dayCalendar["CAS_ZAP_" + str(i)])
                endTime = parseTime(dayCalendar["CAS_VYP_" + str(i)])
                hdo = hdo or timeInRange(start=startTime, end=endTime, x=checkedTime)
            break
    return hdo

def validity(jsonCalendar):
    """
    :return PLATNOST item for actual weekday
    """
    daytime = datetime.datetime.now(tz=CEZ_TIMEZONE)
    checkedTime = daytime.time()
    response = ""

    for dayCalendar in jsonCalendar:
        firstLastDay = dayCalendar["PLATNOST"]
        if isDay(firstLastDay,daytime.weekday()):
            response = firstLastDay
            break
    return response

