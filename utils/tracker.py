import os
import json
from datetime import datetime

BALANCE_FILE = "balance_log.json"

def _get_hour_key():
    return datetime.now().strftime("%Y-%m-%d %H:00")

def _load_data():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return json.load(f)
    return {}

def _save_data(data):
    with open(BALANCE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_balance(balance):
    data = _load_data()
    hour = _get_hour_key()
    data[hour] = balance
    _save_data(data)

def report_hourly():
    data = _load_data()
    hours = sorted(data.keys())
    if len(hours) < 2:
        return  # Need at least 2 entries to compare

    current = hours[-1]
    previous = hours[-2]

    p_start = data[previous]
    p_end = data[current]
    diff = round(p_end - p_start, 2)

    print(f"\n📊 P&L Report [{current}]")
    print(f"• Start:  ${p_start}")
    print(f"• End:    ${p_end}")
    print(f"• Profit: ${diff if diff >= 0 else '-' + str(abs(diff))}")
