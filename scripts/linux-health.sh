#!/usr/bin/env bash
set -euo pipefail
echo "hostname=$(hostname)"
echo "uptime=$(uptime -p)"
echo "load=$(awk '{print $1,$2,$3}' /proc/loadavg)"
echo "memory=$(free -h | awk '/Mem:/ {print $3"/"$2}')"
echo "disk=$(df -h / | awk 'NR==2 {print $5" used"}')"
