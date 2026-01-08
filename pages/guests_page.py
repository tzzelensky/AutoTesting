import pytest
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class GuestsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.find_guest_title = page.locator("h1:has-text('Справочник гостей')")
        self.segment_redirect_button = page.locator('a:has-text("Сегменты")')
        self.phone_number_input = page.locator('input[name="GuestsCustomerSamples[customer_phone][]"]')



    def check_guest_admin_title(self):
        expect(self.find_guest_title).to_be_visible()
        expect(self.find_guest_title).to_have_text('Справочник гостей')
