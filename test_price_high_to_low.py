from playwright.sync_api._generated import Page


def test_price_high_to_low(page: Page):
    # Select High to Low sorting
    page.select_option('select[data-test="product-sort-container"]', 'hilo')

    # Get all product prices
    prices = page.locator('.inventory_item_price').all_text_contents()
    price_values = [float(price[1:]) for price in prices]  # remove $ sign

    expected = sorted(price_values, reverse=True)
    assert price_values == expected, "Prices are not sorted high to low"