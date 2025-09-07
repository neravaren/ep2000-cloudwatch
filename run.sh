#!/bin/bash
PATH=/home/pi/.local/bin:$PATH
cd /home/pi/ep2000-cloudwatch
uv run read.py
