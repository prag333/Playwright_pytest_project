import pytest
import subprocess
import os
from pathlib import Path
from playwright.sync_api import sync_playwright
import logging
import allure
from io import StringIO


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="https://www.pfizerforall.com/", help="Base URL for the test run")
    parser.addoption("--headless-mode", action="store", default="True", help="Base URL for the test run")


@pytest.fixture(scope="session")
def BASE_URL(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    """Fixture to set up and tear down the Playwright browser for each test."""

    headless_mode = request.config.getoption('--headless-mode', default=True)
    headless_mode = headless_mode.lower() == 'true'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        yield page
        # Close browser
        page.close()
        browser.close()


def pytest_sessionfinish(session, exitstatus):
    """Called after the whole test run finishes."""

    # Only run report generation if this is the master process
    if not hasattr(session.config, 'workerinput'):
        result_dir = Path("allure-results")
        report_dir = Path("allure-report")

        result_dir.mkdir(parents=True, exist_ok=True)
        report_dir.mkdir(parents=True, exist_ok=True)

        subprocess.run(["allure", "generate", str(result_dir), "--clean", "-o", str(report_dir)], check=True)
        print(f"Allure report generated at: {report_dir.resolve()}")

        if not os.environ.get("CI"):
            print("Opening Allure report in browser...")
            subprocess.Popen(["allure", "serve", str(result_dir)])


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    # Create a log stream per test item
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s", "%H:%M:%S")
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    # Store handler and stream for teardown
    item._log_handler = handler
    item._log_stream = log_stream


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
    logger = logging.getLogger()

    if hasattr(item, "_log_handler"):
        logger.removeHandler(item._log_handler)

    if hasattr(item, "_log_stream"):
        log_text = item._log_stream.getvalue()
        if log_text.strip():
            allure.attach(
                log_text,
                name=f"Logs - {item.name}",
                attachment_type=allure.attachment_type.TEXT
            )

