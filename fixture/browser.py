import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright, Browser, BrowserContext

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    # Фикстура используется для авторизации в системе учета

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://k8s-devtest1.goulash.tech/')

    login_auth_form_fill = page.locator('#LoginForm_username')
    login_auth_form_fill.fill('test')

    password_auth_form_fill = page.locator('#LoginForm_password')
    password_auth_form_fill.fill('1')

    button_auth_form_click = page.locator('#login-submit')
    button_auth_form_click.click()

    context.storage_state(path='browser-state.json')
    browser.close()

@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright, request: SubRequest) -> Page:
    # Фикстуру необходимо передавать в тест

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=False, snapshots=False, sources=False)
    yield context.new_page()
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()
