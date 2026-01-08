import pytest
from playwright.sync_api import Page

from pages.guests_page import GuestsPage


@pytest.fixture
def guests_page(chromium_page_with_state: Page) -> GuestsPage:
    return GuestsPage(page=chromium_page_with_state)
