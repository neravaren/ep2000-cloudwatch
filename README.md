# Ups Metrics for EP2000

Solution for automatic sending metrics from `Must EP2000Pro` UPS to Home Assistant (MQTT) or AWS CloudWatch.

## Configuration

Create a copy of `.env.sample` named as `.env` and update with actual values:
- `MQTT_*` for Home Assistant MQTT (`sendMQTT.py`).
- `AWS_*` for CloudWatch (`sendCW.py`).

## Read Metrics

Launch example:
```bash
export UPS_PORT="/dev/ttyUSB0"
uv run read.py
```

Sample output:
```json
{
    "Time": "2024-05-20T10:20:23.522339+00:00",
    "MachineType": "0000",
    "SoftwareVersion": "16710",
    "WorkState": "LINE",
    "BatClass": "12V",
    "RatedPower": 1000,
    "GridVoltage": 215.0,
    "GridFrequency": 49.8,
    "OutputVoltage": 215.6,
    "OutputFrequency": 49.8,
    "LoadCurrent": 0.1,
    "LoadPower": 27,
    "LoadPercent": 2,
    "LoadState": "LOAD_NORMAL",
    "BatteryVoltage": 13.6,
    "BatteryCurrent": 1.6,
    "BatterySoc": 100,
    "TransformerTemp": 39,
    "AvrState": "AVR_BYPASS",
    "BuzzerState": "BUZZ_OFF",
    "Fault": "",
    "Alarm": "0000",
    "ChargeState": "FV",
    "ChargeFlag": "Charge",
    "MainSw": "Off",
    "DelayType": "Long delay",
    "GridFrequencyType": "50Hz",
    "GridVoltageType": 220,
    "BulkChargeCurrent": 30,
    "BatteryLowVoltage": 10.5,
    "ConstantChargeVoltage": 14.1,
    "FloatChargeVoltage": 13.6,
    "BuzzerSilence": "Silence",
    "EnableGridCharge": "Enable",
    "EnableKeySound": "Enable",
    "EnableBacklight": "Enable"
}
```

## Send Metrics to Home Assistant (MQTT)

Launch example:
```bash
export UPS_PORT="/dev/ttyUSB0"
uv run sendMQTT.py
```

Each run publishes:
- Discovery config (retained) to `homeassistant/<sensor|binary_sensor>/must_ep2000/<metric>/config`. Home Assistant creates the device `Must EP2000` with all entities.
- All metrics as one JSON message to `must_ep2000/state`.

Entities show as unavailable if no update comes for 120 seconds.

Optional settings: `MQTT_DISCOVERY_PREFIX` (default `homeassistant`), `MQTT_DEVICE_ID` (default `must_ep2000`).

## Send Metrics to CloudWatch

Launch example:
```bash
export UPS_PORT="/dev/ttyUSB0"
export METRIC_NAMESPACE="Home/UPS/EP20"
uv run sendCW.py
```

Output Metrics:
- WorkState
- GridVoltage
- GridFrequency
- LoadCurrent
- LoadPower
- LoadPercent
- BatteryVoltage
- BatteryCurrent
- BatterySoc
- TransformerTemp

## Tests

```bash
uv run pytest
```

## Cron

`run.sh` runs `sendMQTT.py`. To use CloudWatch, change the line in `run.sh`.

Sample CRON task described in file `upsMetrics.cron`. Copy to `/etc/cron.d/` and change path inside to actual one.
