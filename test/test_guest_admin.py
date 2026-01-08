import pytest

from pages.guests_page import GuestsPage


@pytest.mark.first_test
def test_find_guest(chromium_page_with_state, guests_page: GuestsPage):
    guests_page.visit('https://k8s-devtest1.goulash.tech/guests/guests/admin')
    guests_page.check_guest_admin_title()
    guests_page.find_guest_on_page()
    guests_page.check_guest_profile()