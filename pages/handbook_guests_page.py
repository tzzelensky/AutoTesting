from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class GuestbookPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.guestbook_page_title = page.get_by_role("heading", name="Справочник гостей")
        self.guestbook_segment_redirect = page.get_by_role("link", name="Сегменты")
        self.guestbook_number_input = page.locator('input[name="GuestsCustomerSamples[customer_phone][]"]').first
        self.guestbook_delete_number_button = page.get_by_alt_text("X")
        self.guestbook_find_guest_button = page.locator('//input[@value="Найти"]')
        self.guestbook_search_by_filter = page.get_by_role("link", name="Поиск по фильтрам")
        self.guestbook_first_guest = page.locator(".items")
        self.guestbook_rfm_analyze_button = page.get_by_role("link", name="RFM анализ")


    def open_guestbook_guest(self):
        self.visit('https://k8s-devtest1.goulash.tech/guests/guests/admin')

    def check_guestbook_page(self):
        expect(self.guestbook_page_title).to_be_visible()

        expect(self.guestbook_segment_redirect).to_be_visible()

        expect(self.guestbook_search_by_filter).to_be_visible()

        expect(self.guestbook_first_guest).to_be_visible()

        expect(self.guestbook_rfm_analyze_button).to_be_visible()


    def find_guest_profile(self):
        expect(self.guestbook_number_input).to_be_visible()
        self.guestbook_number_input.fill('9090104904')

        expect(self.guestbook_find_guest_button).to_be_visible()
        self.guestbook_find_guest_button.click()


