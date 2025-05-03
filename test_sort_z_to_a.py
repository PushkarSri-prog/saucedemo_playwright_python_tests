from playwright.sync_api._generated import Page


def test_sort_z_to_a(page: Page):
    # Select Z to A from dropdown
    page.select_option('select[data-test="product-sort-container"]', 'za')

    # Capture product names
    items = page.locator('.inventory_item_name').all_text_contents()
    expected = sorted(items, reverse=True)

    assert items == expected, "Items are not sorted from Z to A"