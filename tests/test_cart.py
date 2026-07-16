from playwright.sync_api import sync_playwright, expect

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"

def test_add_item_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.get_by_role("button", name="Add to cart").first.click()

        expect(page.get_by_role("button", name="Remove").first).to_be_visible()
        expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")

        browser.close()


def test_remove_item_from_cart():

    """TC-014: Remove item from cart reverts button state and clears badge."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.get_by_role("button", name="Add to cart").first.click()

        page.get_by_role("button", name="Remove").first.click()

        expect(page.get_by_role("button", name="Add to cart").first).to_be_visible()
        expect(page.locator("[data-test='shopping-cart-badge']")).not_to_be_visible()

        browser.close()



