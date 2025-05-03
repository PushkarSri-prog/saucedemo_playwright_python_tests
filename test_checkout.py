from playwright.sync_api._generated import Page


def test_checkout_journey(page: Page):
    # Add two items to cart
    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('button[data-test="add-to-cart-sauce-labs-bike-light"]')
    page.click('button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    page.click('button[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
    page.click('button[data-test="add-to-cart-sauce-labs-onesie"]')

    # Go to cart
    page.click('a[class="shopping_cart_link"]')

    # Verify 2 items in cart
    cart_items = page.locator('.cart_item').count()
    assert cart_items == 5

    # Proceed to checkout
    page.click('button[data-test="checkout"]')
    page.fill('input[data-test="firstName"]', 'Pushkar')
    page.fill('input[data-test="lastName"]', 'Srivastava')
    page.fill('input[data-test="postalCode"]', '224001')
    page.click('input[data-test="continue"]')

    # Verify total label is visible
    assert page.locator('.summary_total_label').is_visible()

    # Finish order
    page.click('button[data-test="finish"]')
    assert page.locator('h2.complete-header').text_content() == "Thank you for your order!"