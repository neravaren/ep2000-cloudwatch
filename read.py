#!/usr/bin/env python

import json
from ep20_api import read_ups_status


# PORT = '/dev/serial0'
# PORT = 'COM3'
PORT = '/dev/ttyUSB0'


if __name__ == '__main__':
    data = read_ups_status(PORT)
    print(json.dumps(data))
