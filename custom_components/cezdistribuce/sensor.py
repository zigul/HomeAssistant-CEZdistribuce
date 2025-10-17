"""Sensor entity exposing upcoming CEZ HDO enable windows."""

from datetime import timedelta
import logging
from typing import Any, Dict, List

import requests
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
import homeassistant.helpers.config_validation as cv
from homeassistant.util import Throttle

from .continuous_measurement import ContinuousMeasurement
from .downloader import CEZ_TIMEZONE, getRequestUrl, get_next_enable_windows

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_SCANS = timedelta(seconds=3600)

DOMAIN = "cezdistribuce"
CONF_REGION = "region"
CONF_CODE = "code"
CONF_NAME = "name"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_REGION): cv.string,
        vol.Required(CONF_CODE): cv.string,
        vol.Required(CONF_NAME): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    "setup upcoming-window sensor platform"
    name = config.get(CONF_NAME)
    region = config.get(CONF_REGION)
    code = config.get(CONF_CODE)

    add_entities([CezDistribuceUpcomingSensor(name, region, code)])


class CezDistribuceUpcomingSensor(SensorEntity):
    "Sensor providing next HDO enable windows"

    _attr_icon = "mdi:calendar-clock"

    def __init__(self, name: str, region: str, code: str):
        self._attr_name = name
        self.region = region
        self.code = code
        self._response_json: Dict[str, Any] = {"data": []}
        self._next_windows: List[Dict[str, str]] = []
        identifier = f"{region}_{code}".replace(" ", "_").lower()
        self._attr_unique_id = f"cezdistribuce_upcoming_{identifier}"
        self.last_update_success = False
        self.update()

    @property
    def native_value(self) -> Any:
        if not self._next_windows:
            return None
        return self._next_windows[0]["start"]

    @property
    def extra_state_attributes(self) -> Dict[str, Any]:
        return {
            "next_windows": self._next_windows,
            "response_json": self._response_json,
            "timezone": str(CEZ_TIMEZONE),
        }

    @property
    def available(self) -> bool:
        return getattr(self, "last_update_success", False)

    @Throttle(MIN_TIME_BETWEEN_SCANS)
    def update(self):
        "refresh schedule data"
        try:
            if self.code in ContinuousMeasurement.isContinuousCode():
                self._response_json = ContinuousMeasurement.getCode(self.code)
                self.last_update_success = True
            else:
                response = requests.get(
                    getRequestUrl(self.region, self.code),
                    timeout=30,
                )
                if response.status_code == 200:
                    self._response_json = response.json()
                    self.last_update_success = True
                else:
                    _LOGGER.warning(
                        "Failed to fetch CEZ data for %s (%s): %s",
                        self.region,
                        self.code,
                        response.status_code,
                    )
                    self.last_update_success = False
                    return
        except requests.RequestException as err:
            _LOGGER.error("Error fetching CEZ schedule for %s: %s", self.code, err)
            self.last_update_success = False
            return

        calendar = self._response_json.get("data", [])
        if not isinstance(calendar, list):
            _LOGGER.debug("Unexpected calendar format for %s: %s", self.code, calendar)
            calendar = []

        windows = get_next_enable_windows(calendar, count=5)
        self._next_windows = windows
        if not windows and calendar:
            _LOGGER.debug("No upcoming windows detected for %s", self.code)
