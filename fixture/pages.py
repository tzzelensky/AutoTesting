import pytest
from playwright.sync_api import Page

from pages.handbook_guests_page import GuestbookPage


@pytest.fixture
def guests_page(chromium_page_with_state: Page) -> GuestbookPage:
    return GuestbookPage(page=chromium_page_with_state)


