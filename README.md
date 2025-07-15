MIST AUTOMATION EXECUTION LIVE REPORT

This Project provides a simple, interactive HTML dashboard for viewing real-time or simulated pytest results. It consists of three main files

## **FILES OVERVIEW**

### 1. 'RealTime Pytest Results.html'

-## **Purpose:** Displays the test exectution summary and detailed resuts in a polished, interactive table.
-**How it works:**
  -Uses JavaScript to fetch test results from 'results.json'
  -Renders a summayr box, (Status, start/end time, counts)
  -Populates a table with each test's details.
  -Failed tests are clickable to sho/hide their exception logs.
  -Uses [DataTables](https://datatables.net/) for sorting, searching, and styling. 
### 2. 'generate_fake_results.py'

- **Purpose:** Generates a fake `results.json` file for demo/testing.
- **How it works:**  
  - Randomly creates test results with a majority passing, a few failing/skipped/in progress.
  - Outputs a JSON file (`results.json`) in the same directory.
  - Run this script to refresh the test data:
    ```
    python generate_fake_results.py
    ```
### 3. `results.json`

- **Purpose:** Stores the test results in JSON format.
- **How it works:**  
  - Contains summary info (status, start/end time, counts).
  - Contains a list of test cases, each with name, status, times, and exception log (if failed).
  - Is read by the HTML dashboard to display results.

---
