import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Скроллим к секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step('Ожидаем секцию "Вопросы о важном"')
    def wait_for_faq_section(self):
        self.find_element_with_wait(MainPageLocators.FAQ_SECTION)

    @allure.step('Кликаем по вопросу')
    def click_faq_question_item(self, question_number):
        question_locator = MainPageLocators.FAQ_QUESTION_ITEMS[question_number]
        self.find_element_with_wait(question_locator).click()

    @allure.step('Ожидаем раскрывающийся ответ')
    def wait_for_faq_answer_item(self, question_number):
        answer_locator = MainPageLocators.FAQ_ANSWER_ITEMS[question_number]
        self.find_element_with_wait(answer_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_item(self, question_number):
        answer_locator = MainPageLocators.FAQ_ANSWER_ITEMS[question_number]
        return self.get_text_from_element(answer_locator)

    @allure.step('Скроллим к секции "Вопросы о важном" и ожидаем ее отображения')
    def scroll_and_wait_for_faq_section(self):
        self.scroll_to_faq_section()
        self.wait_for_faq_section()

    @allure.step('Кликаем по кнопке заказа в хэдере')
    def click_header_order_button(self):
        locator = MainPageLocators.HEADER_ORDER_BUTTON
        self.find_element_with_wait(locator).click()

    @allure.step('Скроллим к кнопке заказа внутри главной страницы')
    def scroll_to_home_order_button(self):
        self.scroll_to_element(MainPageLocators.HOME_ORDER_BUTTON)

    @allure.step('Ожидаем появления и кликаем по кнопке заказа внутри страницы')
    def wait_and_click_home_order_button(self):
        locator = MainPageLocators.HOME_ORDER_BUTTON
        self.find_element_with_wait(locator).click()

    @allure.step('Скроллим к кнопке заказа внутри главной страницы, ожидаем ее отображения и кликаем по ней')
    def scroll_and_click_home_order_button(self):
        self.scroll_to_home_order_button()
        self.wait_and_click_home_order_button()
