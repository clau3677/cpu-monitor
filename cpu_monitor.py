"""cpu_monitor.py

Script sencillo para monitorear el uso de CPU en tiempo real.

Requisitos:
- psutil (pip install psutil)

Ejemplo de uso:
    python3 cpu_monitor.py --interval 2 --duration 30
"""

import argparse
import time
import psutil


def monitor(interval: int, duration: int):
    """Muestra el porcentaje de uso de CPU cada *interval* segundos.

    Args:
        interval (int): segundos entre lecturas.
        duration (int): tiempo total de monitoreo en segundos.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        cpu = psutil.cpu_percent(interval=None)
        print(f"CPU: {cpu:5.1f}%")
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitoreo de uso de CPU")
    parser.add_argument("--interval", type=int, default=1,
                        help="Segundos entre lecturas (default: 1)")
    parser.add_argument("--duration", type=int, default=60,
                        help="Duración total del monitoreo en segundos (default: 60)")
    args = parser.parse_args()
    try:
        monitor(args.interval, args.duration)
    except KeyboardInterrupt:
        print("\nMonitoreo interrumpido por el usuario.")
