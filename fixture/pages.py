import pytest
from playwright.sync_api import Page

from fixture.browser import chromium_page
from pages.guests_page import GuestsPage


@pytest.fixture
def guests_page(chromium_page: Page) -> GuestsPage:
    return GuestsPage(page=chromium_page)
