from datetime import datetime
import os

LOG_FILE = "logs/activity.log"

def log(action):
    os.makedirs("logs", exist_ok=True)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time}] {action}\n")
