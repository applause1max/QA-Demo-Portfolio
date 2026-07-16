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


def test_sort_name_descending():
    
    """TC-008: Verify sorting in descending order"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.locator("[data-test='product-sort-container']").select_option("za")

        products = page.locator("[data-test='inventory-item-name']").all_text_contents()

        assert products == sorted(products, reverse=True)

        browser.close()


def test_sort_price_ascending():

    """TC-009: Verify sorting by price in ascending order"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()


        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.locator("[data-test='product-sort-container']").select_option("lohi")

        pricing = page.locator("[data-test='inventory-item-price']").all_text_contents()

        prices = []
        for price in pricing:
            clean_price = price.replace("$", "")
            number = float(clean_price)
            prices.append(number)

        assert prices == sorted(prices)

        browser.close()



def test_sort_price_descending():

    """TC-010: Verify sorting by price in descending order"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.locator("[data-test='product-sort-container']").select_option("hilo")

        pricing = page.locator("[data-test='inventory-item-price']").all_text_contents()

        prices = []
        for price in pricing:
            clean_price = price.replace("$", "")
            number = float(clean_price)
            prices.append(number)


        assert prices == sorted(prices, reverse=True)

        browser.close()


def test_sort_price_return():

    """
    TC-011: Verify sorting applied when navigating back from product page
    
    NOTE: This test documents actual (buggy) behavior, see BUG-001.
    Sort order was expected to persist, but resets to default instead.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
        page.get_by_role("textbox", name="Password").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.locator("[data-test='product-sort-container']").select_option("lohi")

       
        page.locator("[data-test='inventory-item-name']").first.click()
        page.get_by_role("button", name="Back to Products").click()

        pricing = page.locator("[data-test='inventory-item-price']").all_text_contents()

        prices = []
        for price in pricing:
            clean_price = price.replace("$", "")
            number = float(clean_price)
            prices.append(number)
        
        # Sort resets to default (Name, A-Z) instead of persisting, per BUG-001
        assert prices == sorted(prices)

        browser.close()
