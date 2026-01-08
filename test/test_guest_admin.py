import pytest

from pages.guests_page import GuestsPage

@pytest.flaky(reruns=2, retry_delay=5)
@pytest.mark.first_test
def test_find_guest(guests_page: GuestsPage):
    guests_page.visit('https://k8s-devtest1.goulash.tech/guests/guests/admin')
    guests_page.check_guest_admin_title()
    guests_page.find_guest_on_page()
    guests_page.check_guest_profile()
