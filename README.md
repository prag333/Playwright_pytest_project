# Playwright + Pytest Automation Framework

This project is an automated testing framework using **Playwright** and **Pytest** for browser automation. It uses **Allure** for generating reports and integrates logging functionality to capture and display logs for each test.


## Setup Instructions

1. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright**:
    ```bash
    python -m playwright install
    ```

## Running the Tests

You can run the tests using **Pytest**. Below are some example commands:

- **Run tests in headless mode** (default):
    ```bash
    pytest tests/test_covid19_inperson_appointment.py --base-url="https://www.pfizerforall.com"
    ```

- **Run tests with UI visible** (non-headless mode):
    ```bash
    pytest tests/test_covid19_inperson_appointment.py --base-url="https://www.pfizerforall.com" --headless-mode="False"
    ```

**Command-line options**:
- `--base-url`: Base URL for the test run (default: `https://www.pfizerforall.com`)
- `--headless-mode`: Run in headless mode (True/False). Default is True.

## Test Reports

After running tests, **Allure** will generate a report. You can view it with the following commands:

1. **Generate Allure report**:
    ```bash
    allure generate allure-results --clean -o allure-report
    ```

2. **Serve the report**:
    ```bash
    allure serve allure-results
    ```

This will start a web server and open the Allure report in your default browser.

## How It Works

- **Playwright**: Automates the browser actions (such as clicking, navigating, and interacting with the webpage).
- **Pytest**: Framework used for test execution, assertion, and hooks to manage setup/teardown.
- **Allure**: Generates visually appealing HTML reports, providing detailed information about each test, including logs and screenshots.
- **Logging**: Logs for each test case are captured and attached to Allure for detailed debugging.
