"""data for continuous measurement

Source data: https://www.cezdistribuce.cz/file/edee/distribuce/cezdistribuce_pasmaplatnostintavt_prubehove_mereni.pdf
Database form: 2024-03-19
"""

import logging

_LOGGER = logging.getLogger(__name__)


class ContinuousMeasurement:  # pylint: disable=R0903
    "hold data for this type of measurement"

    @staticmethod
    def isContinuousCode() -> list:
        "list all codes in defined in this type"
        return ContinuousMeasurement.CODES.keys()

    @staticmethod
    def getCode(code: str) -> dict:
        "return specific dict for code or empty dict if code not exists"
        to_response = {"data": ContinuousMeasurement.CODES.get(code)}
        _LOGGER.debug("select data for code %s: %s", code, to_response)
        return to_response

    AKU8V1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "19:00",
        "CAS_VYP_2": "21:00",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    AKU8V2: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "5:00",
        "CAS_ZAP_2": "18:00",
        "CAS_VYP_2": "20:00",
        "CAS_ZAP_3": "23:00",
        "CAS_VYP_3": "23:59",
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    AKU8V3: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "4:00",
        "CAS_ZAP_2": "17:00",
        "CAS_VYP_2": "19:00",
        "CAS_ZAP_3": "22:00",
        "CAS_VYP_3": "23:59",
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    AKU8V4: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "22:00",
        "CAS_VYP_2": "23:59",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    AKU8V5: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "1:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "18:00",
        "CAS_VYP_2": "21:00",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    AKU8V6: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "3:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "15:00",
        "CAS_VYP_2": "18:00",
        "CAS_ZAP_3": "21:00",
        "CAS_VYP_3": "23:00",
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    EMOV1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "2:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "22:00",
        "CAS_VYP_2": "23:00",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    AKU16V1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "8:00",
        "CAS_ZAP_2": "13:00",
        "CAS_VYP_2": "16:00",
        "CAS_ZAP_3": "19:00",
        "CAS_VYP_3": "23:59",
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    PTV1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "9:00",
        "CAS_ZAP_2": "10:00",
        "CAS_VYP_2": "11:00",
        "CAS_ZAP_3": "12:00",
        "CAS_VYP_3": "13:00",
        "CAS_ZAP_4": "14:00",
        "CAS_VYP_4": "16:00",
        "CAS_ZAP_5": "17:00",
        "CAS_VYP_5": "23:59",
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    PTV2: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "7:00",
        "CAS_VYP_2": "9:00",
        "CAS_ZAP_3": "10:00",
        "CAS_VYP_3": "13:00",
        "CAS_ZAP_4": "14:00",
        "CAS_VYP_4": "16:00",
        "CAS_ZAP_5": "17:00",
        "CAS_VYP_5": "23:59",
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    PTV3: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "8:00",
        "CAS_ZAP_2": "9:00",
        "CAS_VYP_2": "12:00",
        "CAS_ZAP_3": "13:00",
        "CAS_VYP_3": "15:00",
        "CAS_ZAP_4": "16:00",
        "CAS_VYP_4": "19:00",
        "CAS_ZAP_5": "20:00",
        "CAS_VYP_5": "23:59",
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    PTV4: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "10:00",
        "CAS_ZAP_2": "11:00",
        "CAS_VYP_2": "12:00",
        "CAS_ZAP_3": "13:00",
        "CAS_VYP_3": "14:00",
        "CAS_ZAP_4": "15:00",
        "CAS_VYP_4": "17:00",
        "CAS_ZAP_5": "18:00",
        "CAS_VYP_5": "23:59",
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    EVV1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "7:00",
        "CAS_VYP_2": "9:00",
        "CAS_ZAP_3": "10:00",
        "CAS_VYP_3": "13:00",
        "CAS_ZAP_4": "14:00",
        "CAS_VYP_4": "16:00",
        "CAS_ZAP_5": "17:00",
        "CAS_VYP_5": "23:59",
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    EVV2: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "8:00",
        "CAS_ZAP_2": "9:00",
        "CAS_VYP_2": "12:00",
        "CAS_ZAP_3": "13:00",
        "CAS_VYP_3": "15:00",
        "CAS_ZAP_4": "16:00",
        "CAS_VYP_4": "19:00",
        "CAS_ZAP_5": "20:00",
        "CAS_VYP_5": "23:59",
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    EVV3: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "10:00",
        "CAS_ZAP_2": "11:00",
        "CAS_VYP_2": "12:00",
        "CAS_ZAP_3": "13:00",
        "CAS_VYP_3": "14:00",
        "CAS_ZAP_4": "15:00",
        "CAS_VYP_4": "17:00",
        "CAS_ZAP_5": "18:00",
        "CAS_VYP_5": "23:59",
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    TCV1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "9:00",
        "CAS_ZAP_2": "10:00",
        "CAS_VYP_2": "12:00",
        "CAS_ZAP_3": "13:00",
        "CAS_VYP_3": "23:59",
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    CHLV1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "3:00",
        "CAS_VYP_1": "23:00",
        "CAS_ZAP_2": None,
        "CAS_VYP_2": None,
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    CHLV2: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "4:00",
        "CAS_ZAP_2": "6:00",
        "CAS_VYP_2": "22:00",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    CHLV3: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "4:30",
        "CAS_ZAP_2": "8:30",
        "CAS_VYP_2": "23:59",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    CHLV4: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "14:00",
        "CAS_ZAP_2": "18:00",
        "CAS_VYP_2": "23:59",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    ZAV1_WORK: dict = {
        "PLATNOST": "Po - Pa",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "10:00",
        "CAS_VYP_2": "23:59",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    ZAV1_WEEK: dict = {
        "PLATNOST": "So - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "23:59",
        "CAS_ZAP_2": None,
        "CAS_VYP_2": None,
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    ZAV2_WORK: dict = {
        "PLATNOST": "Po - Pa",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "3:00",
        "CAS_ZAP_2": "7:00",
        "CAS_VYP_2": "23:59",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    ZAV2_WEEK: dict = {
        "PLATNOST": "So - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "23:59",
        "CAS_ZAP_2": None,
        "CAS_VYP_2": None,
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    VIKV1_1: dict = {
        "PLATNOST": "Pa - Pa",
        "CAS_ZAP_1": "12:00",
        "CAS_VYP_1": "23:59",
        "CAS_ZAP_2": None,
        "CAS_VYP_2": None,
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    VIKV1_2: dict = {
        "PLATNOST": "So - So",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "23:59",
        "CAS_ZAP_2": None,
        "CAS_VYP_2": None,
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    VIKV1_3: dict = {
        "PLATNOST": "Ne - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "22:00",
        "CAS_ZAP_2": None,
        "CAS_VYP_2": None,
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    VYRV1: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "6:00",
        "CAS_ZAP_2": "10:00",
        "CAS_VYP_2": "16:00",
        "CAS_ZAP_3": "20:00",
        "CAS_VYP_3": "23:59",
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    VYRV2: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "7:00",
        "CAS_ZAP_2": "15:00",
        "CAS_VYP_2": "23:59",
        "CAS_ZAP_3": None,
        "CAS_VYP_3": None,
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }
    VYRV3: dict = {
        "PLATNOST": "Po - Ne",
        "CAS_ZAP_1": "0:00",
        "CAS_VYP_1": "7:00",
        "CAS_ZAP_2": "10:00",
        "CAS_VYP_2": "18:00",
        "CAS_ZAP_3": "23:00",
        "CAS_VYP_3": "23:59",
        "CAS_ZAP_4": None,
        "CAS_VYP_4": None,
        "CAS_ZAP_5": None,
        "CAS_VYP_5": None,
        "CAS_ZAP_6": None,
        "CAS_VYP_6": None,
        "CAS_ZAP_7": None,
        "CAS_VYP_7": None,
        "CAS_ZAP_8": None,
        "CAS_VYP_8": None,
        "CAS_ZAP_9": None,
        "CAS_VYP_9": None,
        "CAS_ZAP_10": None,
        "CAS_VYP_10": None,
    }

    # define global data with all continuous measurements
    CODES: dict = {
        "AKU8V1": [AKU8V1],
        "AKU8V2": [AKU8V2],
        "AKU8V3": [AKU8V3],
        "AKU8V4": [AKU8V4],
        "AKU8V5": [AKU8V5],
        "AKU8V6": [AKU8V6],
        "EMOV1": [EMOV1],
        "AKU16V1": [AKU16V1],
        "PTV1": [PTV1],
        "PTV2": [PTV2],
        "PTV3": [PTV3],
        "PTV4": [PTV4],
        "EVV1": [EVV1],
        "EVV2": [EVV2],
        "EVV3": [EVV3],
        "TCV1": [TCV1],
        "CHLV1": [CHLV1],
        "CHLV2": [CHLV2],
        "CHLV3": [CHLV3],
        "CHLV4": [CHLV4],
        "ZAV1": [ZAV1_WORK, ZAV1_WEEK],
        "ZAV2": [ZAV2_WORK, ZAV2_WEEK],
        "VIKV1": [VIKV1_1, VIKV1_2, VIKV1_3],
        "VYRV1": [VYRV1],
        "VYRV2": [VYRV2],
        "VYRV3": [VYRV3],
    }
