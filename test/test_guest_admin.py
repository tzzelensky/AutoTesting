import pytest


from pages.handbook_guests_page import GuestbookPage

@pytest.mark.first_test
def test_find_guest(guests_page: GuestbookPage):
    guests_page.visit('https://k8s-devtest1.goulash.tech/guests/guests/admin')
    guests_page.check_guestbook_page()
    guests_page.find_guest_profile()
