import pytest
from playwright.sync_api import Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope="session")
def  open_system(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://k8s-devtest1.goulash.tech/')

    page.locator('#LoginForm_username').fill('test')
    page.locator('#LoginForm_password').fill('1')
    page.locator('#login-submit').click()
    yield page
    browser.close()