#!/bin/bash

# Set
PATH=/home/revenant/.local/bin:$PATH
LOGFILE="/tmp/ep2000-cloudwatch-last-run.log"
LOCKFILE="/tmp/ep2000-cloudwatch.lock"
MAXSIZE=$((512 * 1024))  # 512 KB in bytes
RUN_TIMEOUT=20           # seconds, must be less than the 30 second cron interval

# Skip this run if the previous run still uses the serial port
exec 9>"$LOCKFILE"
if ! flock -n 9; then
    echo "$(date) skipped: previous run is still active" >> "$LOGFILE"
    exit 0
fi

# Truncate if log is too big
if [ -f "$LOGFILE" ] && [ $(stat -c%s "$LOGFILE") -gt $MAXSIZE ]; then
    > "$LOGFILE"
fi

# Run
cd /home/revenant/ep2000-cloudwatch || exit 1
echo  "/======= $(date) =======\\" >> "$LOGFILE"
# timeout -k 5 "$RUN_TIMEOUT" uv run read.py >> "$LOGFILE" 2>&1
# timeout -k 5 "$RUN_TIMEOUT" uv run sendCW.py >> "$LOGFILE" 2>&1
timeout -k 5 "$RUN_TIMEOUT" uv run sendMQTT.py >> "$LOGFILE" 2>&1
STATUS=$?
if [ $STATUS -eq 124 ]; then
    echo "Killed: run took more than $RUN_TIMEOUT seconds" >> "$LOGFILE"
fi
echo "\\======= $(date) =======/" >> "$LOGFILE"
