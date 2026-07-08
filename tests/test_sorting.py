from playwright.sync_api import sync_playwright, expect

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"

def test_sort_name_ascending():

    """TC-007: Verify sorting in ascending order"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.locator("[data-test='product-sort-container']").select_option("az")

        products = page.locator("[data-test='inventory-item-name']").all_text_contents()

        assert products == sorted(products)

        browser.close()

