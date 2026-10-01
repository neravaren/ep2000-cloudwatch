#!/usr/bin/env python

import json
import os
import threading
from dotenv import load_dotenv
load_dotenv()

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

from ep20_api import read_ups_status


MQTT_HOST = os.getenv('MQTT_HOST', 'homeassistant.local')
MQTT_PORT = int(os.getenv('MQTT_PORT', '1883'))
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
MQTT_DISCOVERY_PREFIX = os.getenv('MQTT_DISCOVERY_PREFIX', 'homeassistant')
MQTT_DEVICE_ID = os.getenv('MQTT_DEVICE_ID', 'must_ep2000')
UPS_PORT = os.getenv('UPS_PORT', '/dev/ttyUSB0')

STATE_TOPIC = f'{MQTT_DEVICE_ID}/state'
TIMEOUT = 5         # seconds to wait for connect and for each publish
EXPIRE_AFTER = 120  # Home Assistant shows "unavailable" if no update in this time


SENSORS = [
    {'key': 'WorkState', 'name': 'Work state', 'icon': 'mdi:power-plug'},
    {'key': 'GridVoltage', 'name': 'Grid voltage', 'unit': 'V', 'device_class': 'voltage'},
    {'key': 'GridFrequency', 'name': 'Grid frequency', 'unit': 'Hz', 'device_class': 'frequency'},
    {'key': 'OutputVoltage', 'name': 'Output voltage', 'unit': 'V', 'device_class': 'voltage'},
    {'key': 'OutputFrequency', 'name': 'Output frequency', 'unit': 'Hz', 'device_class': 'frequency'},
    {'key': 'LoadCurrent', 'name': 'Load current', 'unit': 'A', 'device_class': 'current'},
    {'key': 'LoadPower', 'name': 'Load power', 'unit': 'W', 'device_class': 'power'},
    {'key': 'LoadPercent', 'name': 'Load', 'unit': '%', 'icon': 'mdi:gauge'},
    {'key': 'LoadState', 'name': 'Load state'},
    {'key': 'BatteryVoltage', 'name': 'Battery voltage', 'unit': 'V', 'device_class': 'voltage'},
    {'key': 'BatteryCurrent', 'name': 'Battery current', 'unit': 'A', 'device_class': 'current'},
    {'key': 'BatterySoc', 'name': 'Battery', 'unit': '%', 'device_class': 'battery'},
    {'key': 'TransformerTemp', 'name': 'Transformer temperature', 'unit': '°C', 'device_class': 'temperature'},
    {'key': 'AvrState', 'name': 'AVR state'},
    {'key': 'ChargeState', 'name': 'Charge state'},
    {'key': 'ChargeFlag', 'name': 'Charge flag'},
    {'key': 'Fault', 'name': 'Fault', 'icon': 'mdi:alert', 'template': "{{ value_json.Fault or 'None' }}"},
]

BINARY_SENSORS = [
    {
        'key': 'GridPower',
        'name': 'Grid power',
        'device_class': 'power',
        'template': "{{ 'ON' if value_json.WorkState == 'LINE' else 'OFF' }}",
    },
]


def build_device(metrics):
    """
    Device block shared by all entities
    """
    return {
        'identifiers': [MQTT_DEVICE_ID],
        'name': 'Must EP2000',
        'manufacturer': 'Must',
        'model': 'EP2000 Pro',
        'sw_version': metrics.get('SoftwareVersion'),
    }


def build_discovery(metrics):
    """
    Build list of (topic, payload) for Home Assistant MQTT discovery
    """
    device = build_device(metrics)
    messages = []
    for component, entities in (('sensor', SENSORS), ('binary_sensor', BINARY_SENSORS)):
        for entity in entities:
            key = entity['key']
            config = {
                'name': entity['name'],
                'unique_id': f'{MQTT_DEVICE_ID}_{key.lower()}',
                'state_topic': STATE_TOPIC,
                'value_template': entity.get('template', f'{{{{ value_json.{key} }}}}'),
                'expire_after': EXPIRE_AFTER,
                'device': device,
            }
            if 'unit' in entity:
                config['unit_of_measurement'] = entity['unit']
                config['state_class'] = 'measurement'
            if 'device_class' in entity:
                config['device_class'] = entity['device_class']
            if 'icon' in entity:
                config['icon'] = entity['icon']
            topic = f'{MQTT_DISCOVERY_PREFIX}/{component}/{MQTT_DEVICE_ID}/{key.lower()}/config'
            messages.append((topic, config))
    return messages


def get_client():
    """
    Connect to MQTT broker, raise if connection or login fails
    """
    result = {}
    connected = threading.Event()

    def on_connect(client, userdata, flags, reason_code, properties):
        result['reason_code'] = reason_code
        connected.set()

    client = mqtt.Client(CallbackAPIVersion.VERSION2, client_id=f'{MQTT_DEVICE_ID}_sender')
    if MQTT_USER:
        client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.on_connect = on_connect
    client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
    client.loop_start()

    if not connected.wait(TIMEOUT):
        client.loop_stop()
        raise TimeoutError(f'No answer from MQTT broker {MQTT_HOST}:{MQTT_PORT}')
    if result['reason_code'].is_failure:
        client.loop_stop()
        raise ConnectionError(f'MQTT connect failed: {result["reason_code"]}')
    return client


def publish(client, topic, payload, retain=False):
    """
    Publish JSON payload and wait for broker acknowledgment
    """
    print(f'[mqtt] publish {topic}')
    info = client.publish(topic, json.dumps(payload), qos=1, retain=retain)
    info.wait_for_publish(timeout=TIMEOUT)
    if not info.is_published():
        raise TimeoutError(f'MQTT publish to {topic} not acknowledged')


def main():
    """
    Main processor
    """
    metrics = read_ups_status(port=UPS_PORT)
    client = get_client()
    try:
        print(f'Sending metrics to MQTT at {metrics["Time"]}')
        for topic, config in build_discovery(metrics):
            publish(client, topic, config, retain=True)
        publish(client, STATE_TOPIC, metrics)
    finally:
        client.disconnect()
        client.loop_stop()
    print('Done')


if __name__ == "__main__":
    main()
