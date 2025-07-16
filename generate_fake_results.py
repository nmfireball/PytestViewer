import json
import random
from datetime import datetime, timedelta

def random_time_pair():
    base_time = datetime.now()
    # Generate end time first (more recent)
    end_time = base_time - timedelta(seconds=random.randint(0, 300))  # Up to 5 mins ago
    # Generate start time up to 60 seconds before end time
    start_time = end_time - timedelta(seconds=random.randint(1, 60))  # 1-60 seconds before end
    return start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')

def single_random_time():
    return (datetime.now() - timedelta(seconds=random.randint(0, 600))).strftime('%Y-%m-%d %H:%M:%S')

total_tests = 100
passed = int(total_tests * 0.90)      # 90% passed
failed = int(total_tests * 0.05)      # 5% failed (5 tests)
skipped = int(total_tests * 0.025)    # 2.5% skipped (2 tests)
inprogress = int(total_tests * 0.025) # 2.5% in progress (3 tests)

test_statuses = (
    ["Passed"] * passed +
    ["Failed"] * failed +
    ["Skipped"] * skipped +
    ["In Progress"] * inprogress
)
random.shuffle(test_statuses)

tests = []
# When creating test cases:
for i, status in enumerate(test_statuses, 1):
    start, end = random_time_pair()
    execution_time = (datetime.strptime(end, '%Y-%m-%d %H:%M:%S') - 
                     datetime.strptime(start, '%Y-%m-%d %H:%M:%S'))
    tests.append({
        "name": f"test_case_{i}",
        "status": status,
        "start_time": start,
        "end_time": end,
        "execution_time": f"{execution_time.seconds // 60:02d}:{execution_time.seconds % 60:02d}",
        "exception_log": (
            "Traceback (most recent call last):\n  ...\nException: Example error"
            if status == "Failed" else ""
        )
    })

# Calculate overall start and end times first
overall_start = single_random_time()
overall_end = (datetime.strptime(overall_start, '%Y-%m-%d %H:%M:%S') + 
              timedelta(minutes=10, seconds=23)).strftime('%Y-%m-%d %H:%M:%S')

data = {
    "status": "Running",
    "start_time": overall_start,
    "end_time": overall_end,
    "overall_time": "00:10:23",
    "passed": sum(1 for t in tests if t["status"] == "Passed"),
    "failed": sum(1 for t in tests if t["status"] == "Failed"),
    "skipped": sum(1 for t in tests if t["status"] == "Skipped"),
    "inprogress": sum(1 for t in tests if t["status"] == "In Progress"),
    "tests": tests
}

with open("results.json", "w") as f:
    json.dump(data, f, indent=2)

