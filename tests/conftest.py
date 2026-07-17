import pytest
from playwright.sync_api import sync_playwright

STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = context.new_page()
        yield page

        failed = request.node.report_call.failed

        if failed:
            trace_path = f"test-results/{request.node.name}-trace.zip"
            context.tracing.stop(path=trace_path)
        else:
            context.tracing.stop()

        context.close()
        browser.close()

@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    report = yield
    setattr(item, "report_" + report.when, report)
    return report


@pytest.fixture
def logged_in_page(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()
    return page