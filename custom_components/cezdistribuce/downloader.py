"""helper download functions"""

import datetime
import unicodedata
from typing import List, Optional, Sequence, Set

try:
    # python 3.9+
    from zoneinfo import ZoneInfo
except ImportError:
    # python 3.6-3.8
    from backports.zoneinfo import ZoneInfo


BASE_URL = "https://www.cezdistribuce.cz/webpublic/distHdo/adam/containers/"
CEZ_TIMEZONE = ZoneInfo("Europe/Prague")

DAY_ORDER: Sequence[str] = ("Po", "Ut", "St", "Ct", "Pa", "So", "Ne")
DAY_INDEX = {day: index for index, day in enumerate(DAY_ORDER)}


def getCorrectRegionName(region):
    "validate region"
    region = region.lower()
    for x in ["zapad", "sever", "stred", "vychod", "morava"]:
        if x in region:
            return x


def getRequestUrl(region, code):
    "create request URI"
    region = getCorrectRegionName(region)
    return BASE_URL + region + "?&code=" + code.upper()


def timeInRange(start, end, x):
    "is time in range"
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def parseTime(date_time_str):
    "parse time from source data"
    if not date_time_str:
        return datetime.time(0, 0)
    normalized = date_time_str.strip()
    if normalized == "24:00":
        return datetime.time(0, 0)
    hour_str, minute_str = normalized.split(":")
    return datetime.time(int(hour_str), int(minute_str))


def _normalize_label(value: str) -> str:
    "normalize unicode day labels to ascii"
    value = value.replace("–", "-").replace("—", "-")
    normalized = unicodedata.normalize("NFKD", value)
    without_marks = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return without_marks.replace(".", "").strip()


def _extract_day_code(token: str) -> Optional[str]:
    "convert label token into day code"
    if not token:
        return None
    candidate = token.strip().split(" ")[0]
    if len(candidate) >= 2:
        candidate = candidate[:2]
    candidate = candidate.capitalize()
    if candidate in DAY_INDEX:
        return candidate
    return None


def _label_to_days(label: str) -> Set[int]:
    "translate CEZ schedule label to weekday indexes"
    if not label:
        return set()
    normalized = _normalize_label(label)
    direct_map = {
        "Po - Pa": {0, 1, 2, 3, 4},
        "Po - Ne": set(range(7)),
        "So - Ne": {5, 6},
    }
    if normalized in direct_map:
        return direct_map[normalized]
    parts = [part for part in normalized.split(",") if part]
    days: Set[int] = set()
    for part in parts:
        if "-" in part:
            start_token, end_token = [token.strip() for token in part.split("-", 1)]
            start = _extract_day_code(start_token)
            end = _extract_day_code(end_token)
            if start is None or end is None:
                continue
            start_index = DAY_INDEX[start]
            end_index = DAY_INDEX[end]
            if start_index <= end_index:
                days.update(range(start_index, end_index + 1))
            else:
                days.update(range(start_index, 7))
                days.update(range(0, end_index + 1))
        else:
            day_code = _extract_day_code(part)
            if day_code is not None:
                days.add(DAY_INDEX[day_code])
    return days or set(range(7))


def _calendar_for_weekday(json_calendar: Sequence[dict], weekday: int) -> Optional[dict]:
    "select calendar entry describing given weekday"
    fallback: Optional[dict] = None
    for entry in json_calendar:
        label = entry.get("PLATNOST", "")
        days = _label_to_days(label)
        if len(days) == 7 and fallback is None:
            fallback = entry
        if weekday in days:
            if len(days) == 7:
                fallback = entry if fallback is None else fallback
            else:
                return entry
    return fallback


def get_next_enable_windows(
    json_calendar: Sequence[dict],
    count: int = 5,
    reference: Optional[datetime.datetime] = None,
) -> List[dict]:
    "collect upcoming enable windows with start/end ISO timestamps"
    if not json_calendar:
        return []
    reference = reference or datetime.datetime.now(tz=CEZ_TIMEZONE)
    results: List[dict] = []
    max_days = 21  # search window to gather enough events
    for day_offset in range(max_days):
        day_dt = reference + datetime.timedelta(days=day_offset)
        schedule = _calendar_for_weekday(json_calendar, day_dt.weekday())
        if not schedule:
            continue
        for period in range(1, 11):
            start_str = schedule.get(f"CAS_ZAP_{period}")
            end_str = schedule.get(f"CAS_VYP_{period}")
            if not start_str or not end_str:
                continue
            start_time = parseTime(start_str)
            end_time = parseTime(end_str)
            start_dt = datetime.datetime.combine(day_dt.date(), start_time, tzinfo=CEZ_TIMEZONE)
            end_dt = datetime.datetime.combine(day_dt.date(), end_time, tzinfo=CEZ_TIMEZONE)
            if end_time <= start_time:
                end_dt += datetime.timedelta(days=1)
            if day_offset == 0 and start_dt <= reference:
                # skip already started windows
                continue
            results.append(
                {
                    "start": start_dt.isoformat(),
                    "end": end_dt.isoformat(),
                }
            )
            if len(results) >= count:
                return results
    return results


def isHdo(jsonCalendar):
    """
    Find out if the HDO is enabled for the current timestamp

    :param jsonCalendar: JSON with calendar schedule from CEZ
    :param daytime: relevant time in "Europe/Prague" timezone to check if HDO is on or not
    :return: bool
    """
    daytime = datetime.datetime.now(tz=CEZ_TIMEZONE)
    # select Mon-Fri schedule or Sat-Sun schedule according to current date
    if daytime.weekday() < 5:
        dayCalendar = next(
            (x for x in jsonCalendar if x["PLATNOST"] == "Po - Pá" or x["PLATNOST"] == "Po - Ne"), None
        )
    else:
        dayCalendar = next(
            (x for x in jsonCalendar if x["PLATNOST"] == "So - Ne" or x["PLATNOST"] == "Po - Ne"), None
        )

    checkedTime = daytime.time()
    hdo = False

    # iterate over scheduled times in calendar schedule
    for i in range(1, 11):
        startTime = parseTime(dayCalendar["CAS_ZAP_" + str(i)])
        endTime = parseTime(dayCalendar["CAS_VYP_" + str(i)])
        hdo = hdo or timeInRange(start=startTime, end=endTime, x=checkedTime)
    return hdo
