from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class CreatePromotionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.promotion_page = page

    # TODO : =  описать страницу создания акции