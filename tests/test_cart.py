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



def test_checkout_happy_path():

    """TC-019: Complete checkout with valid information and items in cart."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.get_by_role("button", name="Add to cart").first.click()
        page.locator("[data-test='shopping-cart-link']").click()
        page.get_by_role("button", name="Checkout").click()
        page.get_by_role("textbox", name="First Name").fill("Test")
        page.get_by_role("textbox", name="Last Name").fill("User")
        page.get_by_role("textbox", name="Zip/Postal Code").fill("90210")
        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name="Finish").click()

        expect(page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")
        expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

        browser.close()



    