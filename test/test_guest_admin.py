import pytest
from pages.handbook_guests_page import GuestbookPage

@pytest.mark.first_test
def test_find_guest(guests_page: GuestbookPage):
    guests_page.open_guestbook_guest()
    guests_page.check_guestbook_page()
    guests_page.find_guest_profile()