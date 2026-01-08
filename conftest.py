import pytest
from playwright.sync_api import Browser, Playwright
pytest_plugins = [
    "fixture.pages",
    'fixture.browser'
]