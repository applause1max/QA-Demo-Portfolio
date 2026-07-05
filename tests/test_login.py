from playwright.sync_api import sync_playwright, expect

STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"

def test_login_valid():

    """ TC-001: Valid login redirects to inventory page. """
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        browser.close()



def test_login_locked_out():

    """TC-002: Locked Out login shows corresponding error and stays within same URL."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(LOCKED_OUT_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        expect(page).to_have_url("https://www.saucedemo.com/")
        expect(page.get_by_text("locked out.")).to_be_visible()

        browser.close()