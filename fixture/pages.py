import pytest
from playwright.sync_api import Page

from pages.create_promotion_page import CreatePromotionPage
from pages.handbook_guests_page import GuestbookPage


@pytest.fixture
def guests_page(chromium_page_with_state: Page) -> GuestbookPage:
    return GuestbookPage(page=chromium_page_with_state)

@pytest.fixture
def create_promotion_page(chromium_page_with_state: Page) -> CreatePromotionPage:
    return CreatePromotionPage(page=chromium_page_with_state)


