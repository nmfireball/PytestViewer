# MIST AUTOMATION EXECUTION LIVE REPORT

This project provides a simple, interactive HTML dashboard for viewing real-time or simulated pytest results. It is designed for easy deployment on GitHub Pages and features a clean, branded UI.

---

## Files Overview

### 1. `index.html` (Main Dashboard)

- **Purpose:** Displays the test execution summary and detailed results in a polished, interactive table.
- **How it works:**  
  - Uses JavaScript to fetch test results from `results.json` (either from GitHub Pages or user upload).
  - Renders a summary box (status, start/end time, counts).
  - Populates a table with each test's details.
  - Failed tests are clickable to show/hide their exception logs.
  - Uses [DataTables](https://datatables.net/) for sorting, searching, and styling.
  - Includes a navigation menu for switching between the dashboard and FAQ.
  - Allows users to upload their own JSON file and validates its structure before displaying results.
  - Footer displays SparkSoft Corp branding.

---

### 2. `faq.html` (Frequently Asked Questions)

- **Purpose:** Provides answers to common questions about the dashboard and its usage.
- **How it works:**  
  - Styled to match the main dashboard, using the same color scheme and Garamond font.
  - Features a navigation menu for easy access to both pages.
  - FAQ items are expandable/collapsible for a clean, interactive experience.
  - Footer matches the main dashboard for consistent branding.

---

### 3. `results.json` (Test Results Data)

- **Purpose:** Stores the test results in JSON format.
- **How it works:**  
  - Contains summary info (status, start/end time, counts).
  - Contains a list of test cases, each with name, status, times, and exception log (if failed).
  - Is read by the dashboard to display results.
  - Can be replaced by user-uploaded files for custom viewing.

---

### 4. `generate_fake_results.py` (Sample Data Generator)

- **Purpose:** Generates a fake `results.json` file for demo/testing.
- **How it works:**  
  - Randomly creates test results with a majority passing, a few failing/skipped/in progress.
  - Outputs a JSON file (`results.json`) in the same directory.
  - Run this script to refresh the test data:
    ```
    python generate_fake_results.py
    ```

---

## How to Use & Deploy

1. **Local Viewing**
   - Open `index.html` in your browser to view the dashboard.
   - Use the "Upload JSON File" button to view your own results.

2. **Deploy on GitHub Pages**
   - Push all files to your GitHub repository.
   - Go to repository **Settings > Pages** and select the branch and root folder.
   - Add an empty `.nojekyll` file to the root to disable Jekyll processing.
   - Your dashboard will be available at `https://yourusername.github.io/your-repo/`.

3. **Switch Between Pages**
   - Use the navigation menu at the top to switch between the dashboard and FAQ.

---

## Customization

- **Branding:**  
  Colors and fonts are set to match SparkSoft Corp’s theme (`#0059a1`, `#e86b31`, `#656f7a`, Garamond).
- **FAQ Content:**  
  Edit `faq.html` to add or update questions and answers.
- **Logo:**  
  Replace the logo image in the footer with your own if desired.

---

## Example JSON Structure

```json
{
  "status": "Running",
  "start_time": "YYYY-MM-DD HH:MM:SS",
  "end_time": "YYYY-MM-DD HH:MM:SS",
  "overall_time": "HH:MM:SS",
  "passed": 90,
  "failed": 5,
  "skipped": 2,
  "inprogress": 3,
  "tests": [
    {
      "name": "test_case_1",
      "status": "Passed",
      "start_time": "YYYY-MM-DD HH:MM:SS",
      "end_time": "YYYY-MM-DD HH:MM:SS",
      "execution_time": "MM:SS",
      "exception_log": ""
    }
    // ...more test cases
  ]
}
```

---

## License

MIT License. See `LICENSE` for details.
