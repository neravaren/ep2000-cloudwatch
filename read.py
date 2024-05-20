#!/usr/bin/env python

import os
import json
from ep20_api import read_ups_status


# UPS_PORT = '/dev/serial0'
# UPS_PORT = 'COM3'
UPS_PORT = os.getenv('UPS_PORT', '/dev/ttyUSB0')


if __name__ == '__main__':
    data = read_ups_status(UPS_PORT)
    print(json.dumps(data))
