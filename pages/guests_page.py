import pytest
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class GuestsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.find_guest_title = page.locator("h1:has-text('Справочник гостей')")
        self.segment_redirect_button = page.locator('a:has-text("Сегменты")')
        self.phone_number_input = page.locator('//input[@name="GuestsCustomerSamples[customer_phone][]"]').first
        self.search_guest_button = page.locator('//input[@value="Найти"]')
        self.guest_profile = page.get_by_title("Просмотреть").first
        self.title_guest_profile = page.get_by_role("heading", name="Карточка гостя")



    def check_guest_admin_title(self):
        expect(self.find_guest_title).to_be_visible()
        expect(self.find_guest_title).to_have_text('Справочник гостей')

    def find_guest_on_page(self):
        expect(self.phone_number_input).to_be_visible()
        self.phone_number_input.fill('9090104904')
        expect(self.search_guest_button).to_be_visible()
        self.search_guest_button.click()

    def check_guest_profile(self):
        expect(self.guest_profile).to_be_visible()
        self.guest_profile.click()
        expect(self.title_guest_profile).to_be_visible()
        expect(self.title_guest_profile).to_have_text('Карточка гостя')
