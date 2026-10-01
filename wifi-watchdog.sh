#!/bin/bash
#
# Wi-Fi watchdog. Run as root from cron every minute.
# - Network OK: reset the failure counter.
# - Network down: restart Wi-Fi.
# - Network down for REBOOT_AFTER checks: reboot.

TARGET="${WATCHDOG_TARGET:-10.2.1.12}"       # host to ping (MQTT broker)
IFACE="${WATCHDOG_IFACE:-wlan0}"
REBOOT_AFTER="${WATCHDOG_REBOOT_AFTER:-10}"  # failed checks before reboot
MIN_UPTIME="${WATCHDOG_MIN_UPTIME:-900}"     # seconds, no reboot before this uptime
STATE_DIR="${WATCHDOG_STATE_DIR:-/run}"      # /run is cleared on reboot
COUNTER_FILE="$STATE_DIR/wifi-watchdog.count"
LOCKFILE="$STATE_DIR/wifi-watchdog.lock"

log() {
    logger -t wifi-watchdog "$1"
    echo "$1"
}

network_ok() {
    # Try the gateway too, so a broker restart alone does not restart Wi-Fi
    local gateway
    gateway=$(ip route show default dev "$IFACE" 2>/dev/null | awk '{print $3; exit}')
    ping -c 3 -W 2 -q "$TARGET" > /dev/null 2>&1 && return 0
    [ -n "$gateway" ] && ping -c 3 -W 2 -q "$gateway" > /dev/null 2>&1 && return 0
    return 1
}

restart_wifi() {
    if command -v nmcli > /dev/null && nmcli -t general status > /dev/null 2>&1; then
        log "restart Wi-Fi with NetworkManager"
        nmcli radio wifi off
        sleep 5
        nmcli radio wifi on
    else
        log "restart Wi-Fi with ip link and wpa_cli"
        ip link set "$IFACE" down
        sleep 5
        ip link set "$IFACE" up
        wpa_cli -i "$IFACE" reconfigure > /dev/null 2>&1
    fi
}

# Only one check at a time
exec 9>"$LOCKFILE"
flock -n 9 || exit 0

if network_ok; then
    if [ -f "$COUNTER_FILE" ]; then
        log "network OK after $(cat "$COUNTER_FILE") failed checks"
        rm -f "$COUNTER_FILE"
    fi
    exit 0
fi

COUNT=$(( $(cat "$COUNTER_FILE" 2>/dev/null || echo 0) + 1 ))
echo "$COUNT" > "$COUNTER_FILE"
log "network check failed ($COUNT of $REBOOT_AFTER)"

UPTIME=$(cut -d. -f1 /proc/uptime)
if [ "$COUNT" -ge "$REBOOT_AFTER" ] && [ "$UPTIME" -ge "$MIN_UPTIME" ]; then
    log "reboot: network down for $COUNT checks"
    sync
    reboot
    exit 0
fi

restart_wifi
