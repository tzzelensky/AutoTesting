import pytest
from playwright.sync_api import Page, expect
from pages.guests_page import GuestsPage

@pytest.mark.first_test
def test_guest_admin_title(guests_page: GuestsPage, open_system):
    guests_page.goto('https://k8s-devtest1.goulash.tech/guests/guests/admin')
    guests_page.find_guest_title()