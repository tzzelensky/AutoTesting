import time

from pages.create_promotion_page import CreatePromotionPage


def test_create_promotion_page(create_promotion_page: CreatePromotionPage):
    unique_index = str(int(time.time()))
    create_promotion_page.open_create_promotion_page()
    create_promotion_page.create_promotion(unique_index)
    create_promotion_page.check_create_promotion('expected_url')
