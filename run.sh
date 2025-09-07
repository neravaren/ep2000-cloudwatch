#!/bin/bash

# Set
PATH=/home/pi/.local/bin:$PATH
LOGFILE="/tmp/ep2000-cloudwatch-last-run.log"
MAXSIZE=$((512 * 1024))  # 512 KB in bytes

# Truncate if log is too big
if [ -f "$LOGFILE" ] && [ $(stat -c%s "$LOGFILE") -gt $MAXSIZE ]; then
    > "$LOGFILE"
fi

# Run
cd /home/pi/ep2000-cloudwatch
echo  "/======= $(date) =======\\" >> "$LOGFILE"
# uv run read.py >> "$LOGFILE" 2>&1
uv run send.py >> "$LOGFILE" 2>&1
echo "\\======= $(date) =======/" >> "$LOGFILE"
