"""cpu-monitor

Simple script that logs CPU usage percentage every 5 seconds to stdout and to a rotating log file.

Requirements:
  - psutil (`pip install psutil`)
  - Python 3.8+
"""
import time
import logging
from logging.handlers import RotatingFileHandler

import psutil

# Configure logger with rotation (5 MB per file, keep 3 backups)
logger = logging.getLogger("cpu_monitor")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("cpu_usage.log", maxBytes=5*1024*1024, backupCount=3)
formatter = logging.Formatter("%(asctime)s - CPU: %(message)s%%")
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    logger.info(str(cpu_percent))
    print(f"CPU usage: {cpu_percent}%")

if __name__ == "__main__":
    print("Starting CPU monitor (logs to cpu_usage.log every 5 seconds)...")
    while True:
        log_cpu()
        time.sleep(5)
