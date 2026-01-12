import re
from re import Pattern

from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class CreatePromotionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        self.promotion_internal_name = page.locator('input[name="Promoevent[name]"]')
        self.promotion_website_name = page.locator('input[name="Promoevent[name_site]"]')
        self.promotion_active_checkbox = page.locator('#Promoevent_is_active')
        self.promotion_type = page.get_by_label("Выберите тип акции *") #выбрать нужный тип акции select_option("")
        self.promotion_code_generate_button = page.get_by_role("button", name="Сгенерировать код")
        self.promotion_promoevent_code_input = page.locator('input[name="Promoevent[_code]"]')
        self.promotion_add_conditions = page.locator('//input[@value="Добавить условие"]').first
        self.promotion_conditions = page.get_by_label("Тип условия *")  #select_option("2")
        self.promotion_order_types = page.get_by_label("Типы заказов") #select_option("9")
        self.promotion_add_reward = page.locator('//input[@value="Добавить вознаграждение"]').first
        self.promotion_reward = page.get_by_label("Тип вознаграждения")#select_option("1")
        self.promotion_discount = page.locator('input[name^="PromoeventReward"][name$="[percentage_discount]"]')
        self.promotion_create_button =  page.locator('//input[@value="Создание акции"]')


    def open_create_promotion_page(self):
        self.visit('https://k8s-devtest1.goulash.tech/promoevent/promoevent/create')

    def create_promotion(self, unique_id: str):
        # Использую ID в имени, чтобы тесты не конфликтовали при повторном запуске, т.е. Меняется каждый - раз название акции
        self.promotion_internal_name.fill(f'AUTO_TEST_{unique_id}')
        self.promotion_website_name.fill(f'AUTO_TEST_SITE_{unique_id}')

        self.promotion_active_checkbox.click()
        self.promotion_type.select_option("1")

        self.promotion_code_generate_button.click()
        expect(self.promotion_promoevent_code_input).not_to_be_empty()

        self.promotion_add_conditions.click()
        self.promotion_conditions.select_option("2")
        self.promotion_order_types.select_option("9")
        self.promotion_add_reward.click()
        self.promotion_reward.select_option('1')
        self.promotion_discount.fill('20')
        self.promotion_create_button.click()

    # Проверка, что страница с акцией прогрузилась, чтобы акция создалась
    def check_create_promotion(self, expected_url: Pattern[str]):
        self.check_current_url(re.compile(r".*/promoevent/promoevent/view/"))

