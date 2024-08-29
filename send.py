#!/usr/bin/env python

import os
from dotenv import load_dotenv
load_dotenv()

from boto3 import session
from botocore.config import Config

from ep20_api import read_ups_status
from ep20_lib import EPWorkState


AWS_REGION = os.getenv('AWS_REGION', 'eu-central-1')
METRIC_NAMESPACE = os.getenv('METRIC_NAMESPACE', 'Home/UPS/EP20')
UPS_PORT = os.getenv('UPS_PORT', '/dev/ttyUSB0')


def get_client():
    """
    Get boto3 config
    """
    config = Config(
        region_name=AWS_REGION,
    )
    client = session.Session().client('cloudwatch', config=config)
    return client


def send_metrics(client, time, name, value, unit):
    """
    Send metric to CloudWatch
    """
    if unit == '%':
        unit_for_metric = 'Percent'
    else:
        unit_for_metric = 'None'

    print(f'[aws][cw] put_metric_data {name} {value}')
    response = client.put_metric_data(
        Namespace=METRIC_NAMESPACE,
        MetricData=[
            {
                'MetricName': name,
                'Timestamp': time,
                'Dimensions': [
                    {
                        'Name': 'Units',
                        'Value': unit
                    },
                ],
                'Value': value,
                'Unit': unit_for_metric,
            },
        ]
    )

    meta = response.get('ResponseMetadata')
    status = meta.get('HTTPStatusCode')
    if status != 200:
        print(f'Error: {status}')
        print(response)
    return status


METRICS_LIST =[
    {'name': 'WorkState', 'unit': 'Line', 'sample': 'LINE', 'fixer': lambda x: 1 if x == 'LINE' else 0},
    {'name': 'GridVoltage', 'unit': 'V', 'sample': 218.0, 'fixer': lambda x: x},
    {'name': 'GridFrequency', 'unit': 'Hz', 'sample': 49.8, 'fixer': lambda x: x},
    {'name': 'LoadCurrent', 'unit': 'A', 'sample': 0.7, 'fixer': lambda x: x},
    {'name': 'LoadPower', 'unit': 'W', 'sample': 97, 'fixer': lambda x: x},
    {'name': 'LoadPercent', 'unit': '%', 'sample': 9, 'fixer': lambda x: x},
    {'name': 'BatteryVoltage', 'unit': 'V', 'sample': 13.5, 'fixer': lambda x: x},
    {'name': 'BatteryCurrent', 'unit': 'A', 'sample': 1.6, 'fixer': lambda x: x},
    {'name': 'BatterySoc', 'unit': '%', 'sample': 100, 'fixer': lambda x: x},
    {'name': 'TransformerTemp', 'unit': 'C', 'sample': 44, 'fixer': lambda x: x},
]


def main():
    """
    Main processor
    """
    metrics = read_ups_status(port=UPS_PORT)
    client = get_client()
    time = metrics['Time']
    print(f'Sending metrics to CloudWatch at {time}')
    for target in METRICS_LIST:
        name = target['name']
        unit = target['unit']
        value = target['fixer'](metrics[name])
        send_metrics(
            client=client,
            time=time,
            name=name,
            value=value,
            unit=unit,
        )
    print('Done')


if __name__ == "__main__":
    main()
