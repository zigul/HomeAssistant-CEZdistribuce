__version__ = "0.2"

import logging
from . import downloader
import voluptuous as vol
from datetime import timedelta, datetime, date
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.util import Throttle

import requests
from lxml import html, etree

MIN_TIME_BETWEEN_SCANS = timedelta(seconds=3600)
_LOGGER = logging.getLogger(__name__)

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
    name = config.get(CONF_NAME)
    region = config.get(CONF_REGION)
    code = config.get(CONF_CODE)

    ents = []
    ents.append(CezDistribuce(name, region, code))
    add_entities(ents)


class CezDistribuce(BinarySensorEntity):
    def __init__(self, name, region, code):
        """Initialize the sensor."""
        self._name = name
        self.region = region
        self.code = code
        self.responseJson = "[]"
        self.update()

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return "mdi:power"

    @property
    def is_on(self):
        return downloader.isHdo(self.responseJson["data"])

    @property
    def extra_state_attributes(self):
        attributes = {}
        attributes["response_json"] = self.responseJson
        return attributes

    @property
    def should_poll(self):
        return True

    @property
    def available(self):
        return self.last_update_success

    @property
    def device_class(self):
        return ""

    @property
    def unique_id(self):
        return "cezdistribuce_" + self._name

    @Throttle(MIN_TIME_BETWEEN_SCANS)
    def update(self):
        # REGION = "regionStred"
        # CODE = "A1B5DP6"

        response = requests.get(downloader.getRequestUrl(self.region, self.code))
        if response.status_code == 200:
            self.responseJson = response.json()
            self.last_update_success = True
        else:
            self.last_update_success = False
