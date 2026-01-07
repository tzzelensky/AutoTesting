import pytest
from playwright.sync_api import Page, expect


class GuestsPage(Page):
    def __init__(self, page:Page):
        super().__init__(page)

        self.find_guest = page.get_by_test_id('v_su_no_test_id_fuck')