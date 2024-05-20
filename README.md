# Ups CloudWatch Metrics for EP2000

Solution for automatic sending metrics from `Must EP2000Pro` UPS to CloudWatch.

## Configuration

AWS Credentials need to be configured. Create a copy of `.env.sample` named as `.env` and update with actual keys.

## Read Metrics

Launch example:
```bash
export UPS_PORT="/dev/ttyUSB0"
python read.py
```

Sample output:
```json
{"Time": "2024-05-20T10:20:23.522339+00:00", "MachineType": "0000", "SoftwareVersion": "16710", "WorkState": "LINE", "BatClass": "12V", "RatedPower": 1000, "GridVoltage": 215.0, "GridFrequency": 49.8, "OutputVoltage": 215.6, "OutputFrequency": 49.8, "LoadCurrent": 0.1, "LoadPower": 27, "LoadPercent": 2, "LoadState": "LOAD_NORMAL", "BatteryVoltage": 13.6, "BatteryCurrent": 1.6, "BatterySoc": 100, "TransformerTemp": 39, "AvrState": "AVR_BYPASS", "BuzzerState": "BUZZ_OFF", "Fault": "", "Alarm": "0000", "ChargeState": "FV", "ChargeFlag": "Charge", "MainSw": "Off", "DelayType": "Long delay", "GridFrequencyType": "50Hz", "GridVoltageType": 220, "BulkChargeCurrent": 30, "BatteryLowVoltage": 10.5, "ConstantChargeVoltage": 14.1, "FloatChargeVoltage": 13.6, "BuzzerSilence": "Silence", "EnableGridCharge": "Enable", "EnableKeySound": "Enable", "EnableBacklight": "Enable"}
```

## Send Metrics

Launch example:
```bash
export UPS_PORT="/dev/ttyUSB0" 
export METRIC_NAMESPACE="Home/UPS/EP20"
python send.py
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

## Cron

Sample CRON task described in file `upsMetrics.cron`. Copy to `/etc/cron.d/` and change path inside to actual one.
