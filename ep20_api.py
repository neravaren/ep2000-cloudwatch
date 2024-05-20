import re
import serial
import time
from datetime import datetime, timezone

from ep20_lib import (
    DEVICE,
    EPWorkState,
    EPLoadState,
    EPAVRState,
    EPChargeState,
    EPChargeFlag,
    EPMainSW,
    EPBuzzerSilence,
    EPBuzzerState,
    FAULT_DICT,
    get_effective_range,
)


SERIAL_LOGS = False


def open_serial(port:str, baudrate:int=9600, timeout:int=1):
    """
    Open serial connection
    """
    connection = serial.Serial(
        port=port,
        baudrate = baudrate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=timeout,
    )
    return connection


class Commands:
    """
    Collection of commands
    """
    COMMAND_1 = {'data': '0A 03 75 30 00 1B 1E B9', 'size': 59}
    COMMAND_2 = {'data': '0A 03 79 18 00 0A 5D ED', 'size': 25}


def to_hex(data):
    """
    Convert bytes to hex string
    """
    return data.hex()


def from_hex(data):
    """
    Convert hex value to int
    """
    return int(data, 16)


def handle_com_returned(hexstrg):
    """
    Helper to format response
    """
    # Remove the first 8 characters
    hexstrg = hexstrg[8:]
    # Remove the last 5 characters
    hexstrg = hexstrg[:-5]
    # Trim the string
    hexstrg = hexstrg.strip()
    # Create a list of characters from the string
    str_list = list(hexstrg)
    # Iterate backwards over the string
    for start_index in range(len(str_list) - 1, -1, -1):
        if start_index % 6 == 2:
            del str_list[start_index]
    # Join the list back into a string
    result_str = ''.join(str_list)
    # Split the string by spaces and return the list
    return result_str.split(' ')


def send_command(connection, command):
    """
    Send command and read response
    """
    text_command = command['data']
    resp_size = command['size']

    # 1
    text_arr = bytearray.fromhex(re.sub(r' ', '', text_command))
    # Send
    if SERIAL_LOGS:
        print(f'[serial][>>] {text_arr}')
    connection.write(text_arr)
    time.sleep(0.3)
    # Read
    resp_data = b''
    resp_data_str = ''
    for i in range(resp_size):
        x = connection.read()
        x_hex = to_hex(x).upper()
        resp_data = resp_data + x
        resp_data_str = resp_data_str + x_hex + ' '
        if len(resp_data) == resp_size:
            break
    if SERIAL_LOGS:
        print(f'[serial][<<] {resp_data_str}')
    return resp_data_str


class Command:
    def __init__(self, connection, payload=None, size=None) -> None:
        self.connection = connection
        self.payload = payload
        self.size = size

    def execute(self):
        resp_data_str = send_command(
            connection=self.connection,
            command={
                'data': self.payload,
                'size': self.size,
            },
        )
        response = self.decode(resp_data_str)
        return response

    def decode(self, response:str):
        """
        Decode response
        """
        raise NotImplementedError()


class CommandOne(Command):
    def __init__(self, connection) -> None:
        self.connection = connection
        self.payload = Commands.COMMAND_1['data']
        self.size = Commands.COMMAND_1['size']
        super().__init__(connection, self.payload, self.size)

    def decode(self, response:str):
        """
        Decode response
        """
        arr_ro = handle_com_returned(response)
        data = {}
        data['MachineType'] = arr_ro[0]
        data['SoftwareVersion'] = str(from_hex(arr_ro[1]))
        data['WorkState'] = EPWorkState(from_hex(arr_ro[2])).name
        data['BatClass'] = f'{from_hex(arr_ro[3])}V'
        data['RatedPower'] = from_hex(arr_ro[4])
        data['GridVoltage'] = round(float(from_hex(arr_ro[5])) * 0.1, 2)
        data['GridFrequency'] = round(float(from_hex(arr_ro[6])) * 0.1, 2)
        data['OutputVoltage'] = round(float(from_hex(arr_ro[7])) * 0.1, 2)
        data['OutputFrequency'] = round(float(from_hex(arr_ro[8])) * 0.1, 2)
        data['LoadCurrent'] = round(float(from_hex(arr_ro[9])) * 0.1, 2)
        data['LoadPower'] = from_hex(arr_ro[10])
        data['LoadPercent'] = from_hex(arr_ro[12])
        data['LoadState'] = EPLoadState(from_hex(arr_ro[13])).name
        data['BatteryVoltage'] = round(float(from_hex(arr_ro[14])) * 0.1, 2)
        data['BatteryCurrent'] = round(float(from_hex(arr_ro[15])) * 0.1, 2)
        data['BatterySoc'] = from_hex(arr_ro[17])
        data['TransformerTemp'] = from_hex(arr_ro[18])
        data['AvrState'] = EPAVRState(from_hex(arr_ro[19])).name
        data['BuzzerState'] = EPBuzzerState(from_hex(arr_ro[20])).name
        data['Fault'] = FAULT_DICT[str(from_hex(arr_ro[21]))]
        data['Alarm'] = format(from_hex(arr_ro[22]), '04b')
        data['ChargeState'] = EPChargeState(from_hex(arr_ro[23])).name
        data['ChargeFlag'] = EPChargeFlag(from_hex(arr_ro[24])).name
        data['MainSw'] = EPMainSW(from_hex(arr_ro[25])).name

        # Find delay type using list comprehension
        range_info = get_effective_range(
            kind=DEVICE,
            name='DelayType',
            id=from_hex(arr_ro[26]),
        )
        data['DelayType'] = range_info.get('Value')

        return data


class CommandTwo(Command):
    def __init__(self, connection) -> None:
        self.connection = connection
        self.payload = Commands.COMMAND_2['data']
        self.size = Commands.COMMAND_2['size']
        super().__init__(connection, self.payload, self.size)

    def decode(self, response:str):
        """
        Decode response
        """
        arr_ro = handle_com_returned(response)
        data = {}

        range_info = get_effective_range(
            kind=DEVICE,
            name='GridFrequencyType',
            id=from_hex(arr_ro[0]),
        )
        data['GridFrequencyType'] = range_info.get('Value')
        data['GridVoltageType'] = from_hex(arr_ro[1])
        data['BulkChargeCurrent'] = from_hex(arr_ro[5])
        data['BatteryLowVoltage'] = round(float(from_hex(arr_ro[2])) * 0.1, 2)
        data['ConstantChargeVoltage'] = round(float(from_hex(arr_ro[3])) * 0.1, 2)
        data['FloatChargeVoltage'] = round(float(from_hex(arr_ro[4]) * 0.1), 2)
        data['BuzzerSilence'] = EPBuzzerSilence(from_hex(arr_ro[6])).name
        data['EnableGridCharge'] = 'Enable' if from_hex(arr_ro[7]) == 0 else 'Disable'
        data['EnableKeySound'] = 'Enable' if from_hex(arr_ro[8]) == 0 else 'Disable'
        data['EnableBacklight'] = 'Disable' if from_hex(arr_ro[9]) == 0 else 'Enable'

        return data


def read_ups_status(port):
    RS485 = open_serial(port)
    data1 = CommandOne(connection=RS485).execute()
    data2 = CommandTwo(connection=RS485).execute()
    dataAll = {'Time': datetime.now(tz=timezone.utc).isoformat(), **data1, **data2}
    return dataAll
