"""
🔱 THERMAL CHECK: Monitors system thermal levels.
This node simulates a hardware check on the Vember-OS core.
"""

import time
import random

def run():
    print("🔱 VEMBER-OS | THERMAL DIAGNOSTIC STARTING...")
    for i in range(5):
        temp = random.randint(30, 75)
        status = "NORMAL" if temp < 70 else "CRITICAL"
        print(f"[SECURE] CPU TEMP: {temp}°C | STATUS: {status}")
        time.sleep(1)
    print("🔱 DIAGNOSTIC COMPLETE.")

if __name__ == "__main__":
    run()