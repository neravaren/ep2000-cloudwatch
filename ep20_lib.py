from enum import Enum


DEVICE = 'Ep2000Pro'


class EPWorkState(Enum):
    INIT = 1
    SELF_CHECK = 2
    BACKUP = 3
    LINE = 4
    STOP = 5
    POWER_OFF = 6
    GRID_CHG = 7
    SOFT_START = 8


class EPLoadState(Enum):
    LOAD_NORMAL = 0
    LOAD_ALARM = 1
    OVER_LOAD = 2


class EPAVRState(Enum):
    AVR_BYPASS = 0
    AVR_STEPDWON = 1
    AVR_BOOST = 2
    AVR_UNKNOWN3 = 3
    AVR_UNKNOWN4 = 4
    AVR_UNKNOWN5 = 5
    AVR_UNKNOWN6 = 6


class EPChargeState(Enum):
    CC = 0
    CV = 1
    FV = 2


class EPChargeFlag(Enum):
    UnCharge = 0
    Charge = 1


class EPMainSW(Enum):
    Off = 0
    On = 1


class EPBuzzerSilence(Enum):
    Normal = 0
    Silence = 1


class EPBuzzerState(Enum):
    BUZZ_OFF = 0
    BUZZ_BLEW = 1
    BUZZ_ALARM = 2


FAULT_DICT = {
    "0": "",
    "1": "Fan is locked when inverter is off",
    "2": "Inverter transformer over temperature",
    "3": "battery voltage is too high",
    "4": "battery voltage is too low",
    "5": "Output short circuited",
    "6": "Inverter output voltage is high",
    "7": "Overload time out",
    "8": "Inverter bus voltage is too high",
    "9": "Bus soft start failed",
    "11": "Main relay failed",
    "21": "Inverter output voltage sensor error",
    "22": "Inverter grid voltage sensor error",
    "23": "Inverter output current sensor error",
    "24": "Inverter grid current sensor error",
    "25": "Inverter load current sensor error",
    "26": "Inverter grid over current error",
    "27": "Inverter radiator over temperature",
    "31": "Solar charger battery voltage class error",
    "32": "Solar charger current sensor error",
    "33": "Solar charger current is uncontrollable",
    "41": "Inverter grid voltage is low",
    "42": "Inverter grid voltage is high",
    "43": "Inverter grid under frequency",
    "44": "Inverter grid over frequency",
    "51": "Inverter over current protection error",
    "52": "Inverter bus voltage is too low",
    "53": "Inverter soft start failed",
    "54": "Over DC voltage in AC output",
    "56": "Battery connection is open",
    "57": "Inverter control current sensor error",
    "58": "Inverter output voltage is too low",
    "61": "Fan is locked when inverter is on.",
    "62": "Fan2 is locked when inverter is on.",
    "63": "Battery is over-charged.",
    "64": "Low battery",
    "67": "Overload",
    "70": "Output power Derating",
    "72": "Solar charger stops due to low battery",
    "73": "Solar charger stops due to high PV voltage",
    "74": "Solar charger stops due to over load",
    "75": "Solar charger over temperature",
    "76": "PV charger communication error",
    "77": "Parameter error"
}

EFFECTIVE_RANGE_LIST = [
    {
        "Kind": "Ep2000Pro",
        "Name": "GridFrequencyType",
        "Id": 0,
        "Value": "50Hz"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "GridFrequencyType",
        "Id": 1,
        "Value": "60Hz"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "GridVoltageType",
        "Id": 0,
        "Value": "220V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "GridVoltageType",
        "Id": 1,
        "Value": "120V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 0,
        "Value": "10.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 1,
        "Value": "10.1V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 2,
        "Value": "10.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 3,
        "Value": "10.3V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 4,
        "Value": "10.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 5,
        "Value": "10.5V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 6,
        "Value": "10.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 7,
        "Value": "10.7V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 8,
        "Value": "10.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 9,
        "Value": "10.9V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 10,
        "Value": "11.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 11,
        "Value": "11.1V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 12,
        "Value": "11.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 13,
        "Value": "11.3V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 14,
        "Value": "11.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 15,
        "Value": "11.5V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 16,
        "Value": "11.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 17,
        "Value": "11.7V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 18,
        "Value": "11.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 19,
        "Value": "11.9V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage12",
        "Id": 20,
        "Value": "12.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 0,
        "Value": "20.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 11,
        "Value": "20.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 2,
        "Value": "20.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 3,
        "Value": "20.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 4,
        "Value": "20.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 5,
        "Value": "21.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 6,
        "Value": "21.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 7,
        "Value": "21.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 8,
        "Value": "21.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 9,
        "Value": "21.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 10,
        "Value": "22.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 11,
        "Value": "22.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 12,
        "Value": "22.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 13,
        "Value": "22.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 14,
        "Value": "22.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 15,
        "Value": "23.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 16,
        "Value": "23.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 17,
        "Value": "23.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 18,
        "Value": "23.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 19,
        "Value": "23.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "ShutdownVoltage24",
        "Id": 20,
        "Value": "24.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 0,
        "Value": "13.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 1,
        "Value": "13.9V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 2,
        "Value": "14.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 3,
        "Value": "14.1V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 4,
        "Value": "14.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 5,
        "Value": "14.3V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 6,
        "Value": "14.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 7,
        "Value": "14.5V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 0,
        "Value": "27.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 1,
        "Value": "27.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 2,
        "Value": "28.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 3,
        "Value": "28.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 4,
        "Value": "28.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 5,
        "Value": "28.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 6,
        "Value": "28.8V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 7,
        "Value": "29.0V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "FloatChargeVoltage12V",
        "Id": 0,
        "Value": "13.5V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "FloatChargeVoltage12V",
        "Id": 1,
        "Value": "13.6V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "FloatChargeVoltage12V",
        "Id": 2,
        "Value": "13.7V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "FloatChargeVoltage24V",
        "Id": 0,
        "Value": "27V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "FloatChargeVoltage24V",
        "Id": 1,
        "Value": "27.2V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "FloatChargeVoltage24V",
        "Id": 2,
        "Value": "27.4V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 0,
        "Value": "5A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 1,
        "Value": "10A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 2,
        "Value": "15A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 3,
        "Value": "20A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 4,
        "Value": "25A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 5,
        "Value": "30A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 6,
        "Value": "2A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 7,
        "Value": "35A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BulkChargeCurrent",
        "Id": 8,
        "Value": "40A"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BuzzerSilence",
        "Id": 0,
        "Value": "Normal"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BuzzerSilence",
        "Id": 1,
        "Value": "Silence"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BatClass",
        "Id": 0,
        "Value": "12V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "BatClass",
        "Id": 1,
        "Value": "24V"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "DelayType",
        "Id": 0,
        "Value": "Standard"
    },
    {
        "Kind": "Ep2000Pro",
        "Name": "DelayType",
        "Id": 1,
        "Value": "Long delay"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 1,
        "Value": "INIT"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 2,
        "Value": "SELF_CHECK"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 3,
        "Value": "BACKUP"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 4,
        "Value": "LINE"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 5,
        "Value": "STOP"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 6,
        "Value": "POWER_OFF"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 7,
        "Value": "CHARGER"
    },
    {
        "Kind": "Pv2000",
        "Name": "WorkState",
        "Id": 8,
        "Value": "SOFT_START"
    },
    {
        "Kind": "Pv2000",
        "Name": "BatClass",
        "Id": 1,
        "Value": "12V"
    },
    {
        "Kind": "Pv2000",
        "Name": "BatClass",
        "Id": 2,
        "Value": "24V"
    },
    {
        "Kind": "Pv2000",
        "Name": "LoadState",
        "Id": 0,
        "Value": "LOAD_NORMAL"
    },
    {
        "Kind": "Pv2000",
        "Name": "LoadState",
        "Id": 1,
        "Value": "LOAD_ALARM"
    },
    {
        "Kind": "Pv2000",
        "Name": "LoadState",
        "Id": 2,
        "Value": "OVER_LOAD"
    },
    {
        "Kind": "Pv2000",
        "Name": "AvrState",
        "Id": 0,
        "Value": "AVR_BYPASS"
    },
    {
        "Kind": "Pv2000",
        "Name": "AvrState",
        "Id": 1,
        "Value": "AVR_STEPDWON"
    },
    {
        "Kind": "Pv2000",
        "Name": "AvrState",
        "Id": 2,
        "Value": "AVR_BOOST"
    },
    {
        "Kind": "Pv2000",
        "Name": "AvrState",
        "Id": 4,
        "Value": "AVR_EBOOST"
    },
    {
        "Kind": "Pv2000",
        "Name": "BuzzerState",
        "Id": 0,
        "Value": "BUZZ_OFF"
    },
    {
        "Kind": "Pv2000",
        "Name": "BuzzerState",
        "Id": 1,
        "Value": "BUZZ_BLEW"
    },
    {
        "Kind": "Pv2000",
        "Name": "BuzzerState",
        "Id": 2,
        "Value": "BUZZ_ALARM"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChargeStage",
        "Id": 0,
        "Value": "CC"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChargeStage",
        "Id": 1,
        "Value": "CV"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChargeStage",
        "Id": 2,
        "Value": "FV"
    },
    {
        "Kind": "Pv2000",
        "Name": "GridChargeFlag",
        "Id": 0,
        "Value": "Grid no charge"
    },
    {
        "Kind": "Pv2000",
        "Name": "GridChargeFlag",
        "Id": 1,
        "Value": "Grid charge"
    },
    {
        "Kind": "Pv2000",
        "Name": "MainSw",
        "Id": 0,
        "Value": "Off"
    },
    {
        "Kind": "Pv2000",
        "Name": "MainSw",
        "Id": 1,
        "Value": "On"
    },
    {
        "Kind": "Pv2000",
        "Name": "DelayType",
        "Id": 0,
        "Value": "Standard"
    },
    {
        "Kind": "Pv2000",
        "Name": "DelayType",
        "Id": 1,
        "Value": "Long delay"
    },
    {
        "Kind": "Pv2000",
        "Name": "PvStart",
        "Id": 0,
        "Value": "No PV selfstart"
    },
    {
        "Kind": "Pv2000",
        "Name": "PvStart",
        "Id": 1,
        "Value": "PV selfstart"
    },
    {
        "Kind": "Pv2000",
        "Name": "PvFlag",
        "Id": 0,
        "Value": "No PV"
    },
    {
        "Kind": "Pv2000",
        "Name": "PvFlag",
        "Id": 1,
        "Value": "Have PV"
    },
    {
        "Kind": "Pv2000",
        "Name": "PvChgFlag",
        "Id": 0,
        "Value": "No PV charge"
    },
    {
        "Kind": "Pv2000",
        "Name": "PvChgFlag",
        "Id": 1,
        "Value": "PV charge"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChgSource",
        "Id": 0,
        "Value": "None"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChgSource",
        "Id": 1,
        "Value": "Solar"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChgSource",
        "Id": 2,
        "Value": "Grid"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChgSource",
        "Id": 3,
        "Value": "Solar&&Grid"
    },
    {
        "Kind": "Pv2000",
        "Name": "OutSource",
        "Id": 0,
        "Value": "None"
    },
    {
        "Kind": "Pv2000",
        "Name": "OutSource",
        "Id": 1,
        "Value": "Solar"
    },
    {
        "Kind": "Pv2000",
        "Name": "OutSource",
        "Id": 2,
        "Value": "Grid"
    },
    {
        "Kind": "Pv2000",
        "Name": "OutSource",
        "Id": 3,
        "Value": "Solar&&Grid"
    },
    {
        "Kind": "Pv2000",
        "Name": "GridFrequencyType",
        "Id": 0,
        "Value": "50HZ"
    },
    {
        "Kind": "Pv2000",
        "Name": "GridFrequencyType",
        "Id": 1,
        "Value": "60HZ"
    },
    {
        "Kind": "Pv2000",
        "Name": "GridVoltageType",
        "Id": 0,
        "Value": "230V"
    },
    {
        "Kind": "Pv2000",
        "Name": "GridVoltageType",
        "Id": 1,
        "Value": "120V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 0,
        "Value": "10.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 11,
        "Value": "10.1V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 2,
        "Value": "10.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 3,
        "Value": "10.3V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 4,
        "Value": "10.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 5,
        "Value": "10.5V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 6,
        "Value": "10.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 7,
        "Value": "10.7V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 8,
        "Value": "10.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 9,
        "Value": "10.9V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 10,
        "Value": "11.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 11,
        "Value": "11.1V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 12,
        "Value": "11.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 13,
        "Value": "11.3V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 14,
        "Value": "11.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 15,
        "Value": "11.5V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 16,
        "Value": "11.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 17,
        "Value": "11.7V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 18,
        "Value": "11.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 19,
        "Value": "11.9V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage12",
        "Id": 20,
        "Value": "12.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 0,
        "Value": "20.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 11,
        "Value": "20.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 2,
        "Value": "20.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 3,
        "Value": "20.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 4,
        "Value": "20.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 5,
        "Value": "21.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 6,
        "Value": "21.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 7,
        "Value": "21.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 8,
        "Value": "21.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 9,
        "Value": "21.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 10,
        "Value": "22.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 11,
        "Value": "22.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 12,
        "Value": "22.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 13,
        "Value": "22.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 14,
        "Value": "22.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 15,
        "Value": "23.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 16,
        "Value": "23.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 17,
        "Value": "23.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 18,
        "Value": "23.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 19,
        "Value": "23.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "ShutdownVoltage24",
        "Id": 20,
        "Value": "24.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 0,
        "Value": "13.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 1,
        "Value": "13.9V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 2,
        "Value": "14.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 3,
        "Value": "14.1V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 4,
        "Value": "14.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 5,
        "Value": "14.3V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 6,
        "Value": "14.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage12",
        "Id": 7,
        "Value": "14.5V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 0,
        "Value": "27.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 1,
        "Value": "27.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 2,
        "Value": "28.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 3,
        "Value": "28.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 4,
        "Value": "28.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 5,
        "Value": "28.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 6,
        "Value": "28.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "AbsorptionChargeVoltage24",
        "Id": 7,
        "Value": "29.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "FloatChargeVoltage12",
        "Id": 0,
        "Value": "13.5V"
    },
    {
        "Kind": "Pv2000",
        "Name": "FloatChargeVoltage12",
        "Id": 1,
        "Value": "13.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "FloatChargeVoltage12",
        "Id": 2,
        "Value": "13.7V"
    },
    {
        "Kind": "Pv2000",
        "Name": "FloatChargeVoltage24",
        "Id": 0,
        "Value": "27V"
    },
    {
        "Kind": "Pv2000",
        "Name": "FloatChargeVoltage24",
        "Id": 1,
        "Value": "27.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "FloatChargeVoltage24",
        "Id": 2,
        "Value": "27.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "BulkCurrent12",
        "Id": 0,
        "Value": "10A"
    },
    {
        "Kind": "Pv2000",
        "Name": "BulkCurrent12",
        "Id": 1,
        "Value": "20A"
    },
    {
        "Kind": "Pv2000",
        "Name": "BulkCurrent12",
        "Id": 2,
        "Value": "30A"
    },
    {
        "Kind": "Pv2000",
        "Name": "BulkCurrent24",
        "Id": 0,
        "Value": "5A"
    },
    {
        "Kind": "Pv2000",
        "Name": "BulkCurrent24",
        "Id": 1,
        "Value": "10A"
    },
    {
        "Kind": "Pv2000",
        "Name": "BulkCurrent24",
        "Id": 2,
        "Value": "15A"
    },
    {
        "Kind": "Pv2000",
        "Name": "Buzzer",
        "Id": 0,
        "Value": "Normal"
    },
    {
        "Kind": "Pv2000",
        "Name": "Buzzer",
        "Id": 1,
        "Value": "Silence"
    },
    {
        "Kind": "Pv2000",
        "Name": "OutPriority",
        "Id": 0,
        "Value": "Solar first"
    },
    {
        "Kind": "Pv2000",
        "Name": "OutPriority",
        "Id": 1,
        "Value": "Grid first"
    },
    {
        "Kind": "Pv2000",
        "Name": "OutPriority",
        "Id": 2,
        "Value": "SBU"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChgPriority",
        "Id": 0,
        "Value": "Solar first"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChgPriority",
        "Id": 1,
        "Value": "Grid first"
    },
    {
        "Kind": "Pv2000",
        "Name": "ChgPriority",
        "Id": 2,
        "Value": "Union chg"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv12",
        "Id": 0,
        "Value": "13.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv12",
        "Id": 1,
        "Value": "13.5V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv12",
        "Id": 2,
        "Value": "13.3V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv12",
        "Id": 3,
        "Value": "13.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv12",
        "Id": 4,
        "Value": "12.8V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv24",
        "Id": 0,
        "Value": "27.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv24",
        "Id": 1,
        "Value": "27.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv24",
        "Id": 2,
        "Value": "26.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv24",
        "Id": 3,
        "Value": "26.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Inv24",
        "Id": 4,
        "Value": "25.6V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid12",
        "Id": 0,
        "Value": "11.7V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid12",
        "Id": 1,
        "Value": "12.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid12",
        "Id": 2,
        "Value": "12.2V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid12",
        "Id": 3,
        "Value": "12.5V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid12",
        "Id": 4,
        "Value": "12.7V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid24",
        "Id": 0,
        "Value": "23.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid24",
        "Id": 1,
        "Value": "24.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid24",
        "Id": 2,
        "Value": "24.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid24",
        "Id": 3,
        "Value": "25.0V"
    },
    {
        "Kind": "Pv2000",
        "Name": "Point2Grid24",
        "Id": 4,
        "Value": "25.4V"
    },
    {
        "Kind": "Pv2000",
        "Name": "KeySound",
        "Id": 0,
        "Value": "Disable"
    },
    {
        "Kind": "Pv2000",
        "Name": "KeySound",
        "Id": 1,
        "Value": "Enable"
    }
]


def get_effective_range(kind, name, id):
    for range_info in EFFECTIVE_RANGE_LIST:
        if range_info['Kind'] == kind and range_info['Name'] == name and range_info['Id'] == id:
            return range_info
    return {}
