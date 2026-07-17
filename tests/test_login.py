from playwright.sync_api import expect

STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"

def test_login_valid(page):

    """TC-001: Valid login redirects to inventory page."""
    
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")



def test_login_locked_out(page):

    """TC-002: Locked Out login shows corresponding error and stays within same URL."""

    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill(LOCKED_OUT_USER)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.get_by_text("locked out.")).to_be_visible()




def test_login_wrong_password(page):

    """TC-003: Invalid login with wrong password."""
    
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
    page.get_by_role("textbox", name="Password").fill("Wrong_password")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.get_by_text("Username and password do not match any user in this service")).to_be_visible()



def test_login_empty_username(page):

    """TC-004: Invalid login with empty username."""

    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.get_by_text("Username is required")).to_be_visible()



def test_login_empty_password(page):

    """TC-005: Invalid login with empty password."""

    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.get_by_text("Password is required")).to_be_visible()


def test_login_empty_fields(page):

    """TC-006: Invalid login with empty fields."""

    page.goto("https://www.saucedemo.com/")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.get_by_text("Username is required")).to_be_visible()
