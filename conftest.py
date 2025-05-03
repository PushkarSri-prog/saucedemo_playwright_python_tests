import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # Uncomment the line below to run in headless mode  
        context = browser.new_context()
        page = context.new_page()

        # Go to login page and login
        page.goto("https://www.saucedemo.com/")
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        yield page
        browser.close()