from playwright.sync_api import expect

def test_sort_name_ascending(logged_in_page):

    """TC-007: Verify sorting in ascending order"""

    logged_in_page.locator("[data-test='product-sort-container']").select_option("az")

    products = logged_in_page.locator("[data-test='inventory-item-name']").all_text_contents()

    assert products == sorted(products)


def test_sort_name_descending(logged_in_page):
    
    """TC-008: Verify sorting in descending order"""

    logged_in_page.locator("[data-test='product-sort-container']").select_option("za")

    products = logged_in_page.locator("[data-test='inventory-item-name']").all_text_contents()

    assert products == sorted(products, reverse=True)
    


def test_sort_price_ascending(logged_in_page):

    """TC-009: Verify sorting by price in ascending order"""

    logged_in_page.locator("[data-test='product-sort-container']").select_option("lohi")

    pricing = logged_in_page.locator("[data-test='inventory-item-price']").all_text_contents()

    prices = []
    for price in pricing:
        clean_price = price.replace("$", "")
        number = float(clean_price)
        prices.append(number)

    assert prices == sorted(prices)



def test_sort_price_descending(logged_in_page):

    """TC-010: Verify sorting by price in descending order"""

    logged_in_page.locator("[data-test='product-sort-container']").select_option("hilo")

    pricing = logged_in_page.locator("[data-test='inventory-item-price']").all_text_contents()

    prices = []
    for price in pricing:
        clean_price = price.replace("$", "")
        number = float(clean_price)
        prices.append(number)


    assert prices == sorted(prices, reverse=True)



def test_sort_price_return(logged_in_page):

    """
    TC-011: Verify sorting applied when navigating back from product page
    
    NOTE: This test documents actual (buggy) behavior, see BUG-001.
    Sort order was expected to persist, but resets to default instead.
    """

    logged_in_page.locator("[data-test='product-sort-container']").select_option("lohi")

    
    logged_in_page.locator("[data-test='inventory-item-name']").first.click()
    logged_in_page.get_by_role("button", name="Back to Products").click()

    pricing = logged_in_page.locator("[data-test='inventory-item-price']").all_text_contents()

    prices = []
    for price in pricing:
        clean_price = price.replace("$", "")
        number = float(clean_price)
        prices.append(number)
    
    # Sort resets to default (Name, A-Z) instead of persisting, per BUG-001
    assert prices == sorted(prices)