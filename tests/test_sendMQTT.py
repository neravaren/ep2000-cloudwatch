import json
import re

import sendMQTT


METRICS = {
    'Time': '2024-05-20T10:20:23.522339+00:00',
    'SoftwareVersion': '16710',
    'WorkState': 'LINE',
    'GridVoltage': 215.0,
    'BatterySoc': 100,
    'Fault': '',
}


def test_discovery_has_one_message_per_entity():
    messages = sendMQTT.build_discovery(METRICS)
    assert len(messages) == len(sendMQTT.SENSORS) + len(sendMQTT.BINARY_SENSORS)
    topics = [topic for topic, _ in messages]
    assert len(set(topics)) == len(topics)
    assert all(re.fullmatch(r'homeassistant/(sensor|binary_sensor)/must_ep2000/\w+/config', t) for t in topics)


def test_discovery_payload_fields():
    configs = {topic: config for topic, config in sendMQTT.build_discovery(METRICS)}
    voltage = configs['homeassistant/sensor/must_ep2000/gridvoltage/config']
    assert voltage['state_topic'] == 'must_ep2000/state'
    assert voltage['value_template'] == '{{ value_json.GridVoltage }}'
    assert voltage['unit_of_measurement'] == 'V'
    assert voltage['device_class'] == 'voltage'
    assert voltage['state_class'] == 'measurement'
    assert voltage['unique_id'] == 'must_ep2000_gridvoltage'
    assert voltage['device']['sw_version'] == '16710'

    work_state = configs['homeassistant/sensor/must_ep2000/workstate/config']
    assert 'unit_of_measurement' not in work_state
    assert 'state_class' not in work_state


def test_discovery_payload_is_json_serializable():
    for _, config in sendMQTT.build_discovery(METRICS):
        json.dumps(config)
