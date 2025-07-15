import json
import random
from datetime import datetime, timedelta

def random_time():
    return (datetime.now() - timedelta(seconds=random.randint(0, 3600))).strftime('%Y-%m-%d %H:%M:%S')

total_tests = 100
passed = int(total_tests * 0.7)      # 70% passed
failed = int(total_tests * 0.2)      # 20% failed
skipped = int(total_tests * 0.05)    # 5% skipped
inprogress = total_tests - (passed + failed + skipped)  # remainder

test_statuses = (
    ["Passed"] * passed +
    ["Failed"] * failed +
    ["Skipped"] * skipped +
    ["In Progress"] * inprogress
)
random.shuffle(test_statuses)

tests = []
for i, status in enumerate(test_statuses, 1):
    tests.append({
        "name": f"test_case_{i}",
        "status": status,
        "start_time": random_time(),
        "end_time": random_time(),
        "execution_time": f"00:0{random.randint(0,5)}:{random.randint(10,59)}",
        "exception_log": (
            "Traceback (most recent call last):\n  ...\nException: Example error"
            if status == "Failed" else ""
        )
    })

data = {
    "status": "Running",
    "start_time": random_time(),
    "end_time": random_time(),
    "overall_time": "00:10:23",
    "passed": sum(1 for t in tests if t["status"] == "Passed"),
    "failed": sum(1 for t in tests if t["status"] == "Failed"),
    "skipped": sum(1 for t in tests if t["status"] == "Skipped"),
    "inprogress": sum(1 for t in tests if t["status"] == "In Progress"),
    "tests": tests
}

with open("results.json", "w") as f:
    json.dump(data, f, indent=2)

