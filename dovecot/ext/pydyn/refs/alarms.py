# MARK: - Alarm conversions

from ..refs import limits

DXL_ALARMS = [
    "Input Voltage Error",
    "Angle Limit Error",
    "Overheating Error",
    "Range Error",
    "Checksum Error",
    "Overload Error",
    "Instruction Error",
]

def bytes2_alarm_codes(value):
    """This unpack a single integer into a list of error code"""
    limits.checkbounds('alarm code bytes', 0, 127, value)

    return tuple(int(c) for c in reversed(bin(value+128)[3:]))

def bytes2_alarm_names(value):
    """This unpack a single integer into a list of error names"""
    byte = bytes2_alarm_codes(value)
    return tuple(alarm_i for byte_i, alarm_i in zip(byte, DXL_ALARMS) if byte_i == 1)

def alarm_names_2bytes(value):
    b = 0
    for a in value:
        b += 2 ** DXL_ALARMS.index(a)
    return b

def alarm_codes_2bytes(value):
    b = 0
    for c in value:
        b += 2 ** c
    return b
