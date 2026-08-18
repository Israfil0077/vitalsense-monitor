"""
Quick test helper — NOT part of the real app.

Simulates the ESP32 sending one heart-rate/SpO2 reading by writing
latest_reading.json, the same file app.py reads from.

Usage:
    python simulate_reading.py            # writes one fresh reading
    python simulate_reading.py --loop     # keeps refreshing every 2s,
                                           # like a finger staying on the sensor

Run this in a separate terminal alongside `streamlit run app.py` to see
the dashboard switch from "Place finger on sensor" to real numbers.
Stop this script (Ctrl+C) and wait ~5 seconds to see it fall back to "--".
"""

import argparse
import json
import random
import time

READING_FILE = "latest_reading.json"


def write_reading():
    reading = {
        "heart_rate": random.randint(72, 84),
        "spo2": random.randint(96, 99),
        "timestamp": time.time(),
    }
    with open(READING_FILE, "w") as f:
        json.dump(reading, f)
    print(f"wrote: {reading}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--loop", action="store_true", help="keep sending readings every 2s")
    args = parser.parse_args()

    if args.loop:
        try:
            while True:
                write_reading()
                time.sleep(2)
        except KeyboardInterrupt:
            print("stopped")
    else:
        write_reading()
