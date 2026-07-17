from playwright.sync_api import expect

def test_add_item_to_cart(logged_in_page):

    logged_in_page.get_by_role("button", name="Add to cart").first.click()

    expect(logged_in_page.get_by_role("button", name="Remove").first).to_be_visible()
    expect(logged_in_page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


def test_remove_item_from_cart(logged_in_page):

    """TC-014: Remove item from cart reverts button state and clears badge."""

    logged_in_page.get_by_role("button", name="Add to cart").first.click()

    logged_in_page.get_by_role("button", name="Remove").first.click()

    expect(logged_in_page.get_by_role("button", name="Add to cart").first).to_be_visible()
    expect(logged_in_page.locator("[data-test='shopping-cart-badge']")).not_to_be_visible()




def test_checkout_happy_path(logged_in_page):

    """TC-019: Complete checkout with valid information and items in cart."""

    logged_in_page.get_by_role("button", name="Add to cart").first.click()
    logged_in_page.locator("[data-test='shopping-cart-link']").click()
    logged_in_page.get_by_role("button", name="Checkout").click()
    logged_in_page.get_by_role("textbox", name="First Name").fill("Test")
    logged_in_page.get_by_role("textbox", name="Last Name").fill("User")
    logged_in_page.get_by_role("textbox", name="Zip/Postal Code").fill("90210")
    logged_in_page.get_by_role("button", name="Continue").click()
    logged_in_page.get_by_role("button", name="Finish").click()

    expect(logged_in_page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
