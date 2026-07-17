from playwright.sync_api import expect

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"

def test_sort_name_ascending(page):

    """TC-007: Verify sorting in ascending order"""

    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()

    page.locator("[data-test='product-sort-container']").select_option("az")

    products = page.locator("[data-test='inventory-item-name']").all_text_contents()

    assert products == sorted(products)


def test_sort_name_descending(page):
    
    """TC-008: Verify sorting in descending order"""

    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill(STANDARD_USER)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()

    page.locator("[data-test='product-sort-container']").select_option("za")

    products = page.locator("[data-test='inventory-item-name']").all_text_contents()

    assert products == sorted(products, reverse=True)
    


def test_sort_price_ascending(page):

    """TC-009: Verify sorting by price in ascending order"""

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



def test_sort_price_descending(page):

    """TC-010: Verify sorting by price in descending order"""

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



def test_sort_price_return(page):

    """
    TC-011: Verify sorting applied when navigating back from product page
    
    NOTE: This test documents actual (buggy) behavior, see BUG-001.
    Sort order was expected to persist, but resets to default instead.
    """

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