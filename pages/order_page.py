import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Получаем тайтл страницы')
    def check_title(self):
        return self.get_page_title()

    @allure.step('Кликаем по лого Самоката в хэдере')
    def click_header_logo_scooter(self):
        logo_locator = OrderPageLocators.HEADER_LOGO_SCOOTER
        self.find_element_with_wait(logo_locator).click()

    @allure.step('Кликаем по лого Яндекса в хэдере')
    def click_header_logo_yandex(self):
        logo_locator = OrderPageLocators.HEADER_LOGO_YANDEX
        self.find_element_with_wait(logo_locator).click()

    @allure.step('Устанавливаем имя')
    def set_name(self, keys):
        element = OrderPageLocators.NAME_INPUT
        self.find_element_with_wait(element).send_keys(keys)

    @allure.step('Устанавливаем фамилию')
    def set_surname(self, keys):
        element = OrderPageLocators.SURNAME_INPUT
        self.find_element_with_wait(element).send_keys(keys)

    @allure.step('Устанавливаем номер телефона')
    def set_address(self, keys):
        element = OrderPageLocators.ADDRESS_INPUT
        self.find_element_with_wait(element).send_keys(keys)

    def set_phone(self, keys):
        element = OrderPageLocators.PHONE_INPUT
        self.find_element_with_wait(element).send_keys(keys)

    @allure.step('Устанавливаем дату заказа вводом ее с клавиатуры')
    def set_date_by_keyboard_input(self, keys):
        element = OrderPageLocators.DATE_INPUT
        self.find_element_with_wait(element).send_keys(keys)
        self.find_element_with_wait(element).send_keys(Keys.RETURN)

    @allure.step('Устанавливаем комментарий для курьера')
    def set_comment(self, keys):
        element = OrderPageLocators.COMMENT_INPUT
        self.find_element_with_wait(element).send_keys(keys)

    @allure.step('Получаем текст заголовка модалки об успешном создании заказа')
    def get_order_modal_title(self):
        title = OrderPageLocators.CONFIRM_ORDER_SUCCESS_MSG_HEADER
        return self.get_text_from_element(title)

    @allure.step('Ожидаем отображения страницы "Для кого самокат"')
    def wait_for_user_form_title(self):
        locator = OrderPageLocators.ORDER_USER_FORM_TITLE
        self.find_element_with_wait(locator)

    @allure.step('Кликаем по полю выбора названию станции')
    def click_metro_station_select(self):
        locator = OrderPageLocators.METRO_STATION_CONTROL
        self.find_element_with_wait(locator).click()

    @allure.step('Вводим несколько первых символов в поле выбора станции')
    def input_metro_station_name(self, keys):
        element = OrderPageLocators.METRO_STATION_INPUT
        self.find_element_with_wait(element).send_keys(keys)

    @allure.step('Кликаем по названию станции в списке')
    def select_station(self):
        locator = OrderPageLocators.METRO_STATION_ITEM
        self.find_element_with_wait(locator).click()

    @allure.step('Устанавливаем станцию вводом с клавиатуры и выбором из саджеста')
    def select_station_from_suggest(self):
        locator = OrderPageLocators.METRO_STATION_SUGGEST
        self.find_element_with_wait(locator).click()

    @allure.step('Устанавливаем станцию метро кликом по полю и выбором из списка')
    def set_metro_station_by_click(self):
        self.click_metro_station_select()
        self.select_station()

    @allure.step('Нажимаем кнопку "Далее" в форме заказа')
    def click_next_button(self):
        locator = OrderPageLocators.ORDER_NEXT_BUTTON
        self.find_element_with_wait(locator).click()

    @allure.step('Кликаем по полю выбора даты аренды скутера')
    def click_date_input(self):
        locator = OrderPageLocators.DATE_INPUT
        self.find_element_with_wait(locator).click()

    @allure.step('Ожидаем отображения поп-апа с календарем')
    def wait_for_calendar_popup(self):
        locator = OrderPageLocators.CALENDAR_POPUP
        self.find_element_with_wait(locator)

    @allure.step('Кликаем по дате в календаре')
    def click_date_in_calendar(self):
        locator = OrderPageLocators.CALENDAR_TEST_ITEM
        self.find_element_with_wait(locator).click()

    @allure.step('Устанавливаем дату аренды скутера, выбором ее в календаре')
    def set_date_from_calendar(self):
        self.click_date_input()
        self.wait_for_calendar_popup()
        self.click_date_in_calendar()

    @allure.step('Ожидаем отображения страницы "Про аренду"')
    def wait_for_rent_form_title(self):
        locator = OrderPageLocators.ORDER_RENT_FORM_TITLE
        self.find_element_with_wait(locator)

    @allure.step('Кликаем по полю выбора срока аренды скутера')
    def click_rent_period_control(self):
        locator = OrderPageLocators.RENT_PERIOD_CONTROL
        self.find_element_with_wait(locator).click()

    @allure.step('Ожидаем отображения дропдауна срока аренды скутера')
    def wait_for_rent_period_dropdown(self):
        locator = OrderPageLocators.RENT_PERIOD_DROPDOWN
        self.find_element_with_wait(locator)

    @allure.step('Кликаем по количеству дней в дропдауне срока аренды скутера')
    def click_rent_period_option(self):
        locator = OrderPageLocators.RENT_PERIOD_DROPDOWN_OPTION
        self.find_element_with_wait(locator).click()

    @allure.step('Устанавливаем срок аренды скутера')
    def set_rent_period(self):
        self.click_rent_period_control()
        self.wait_for_rent_period_dropdown()
        self.click_rent_period_option()

    @allure.step('Выбираем цвет скутера, кликом в чекбокс')
    def set_scooter_color(self):
        locator = OrderPageLocators.COLOR_OPTION
        self.find_element_with_wait(locator).click()

    @allure.step('Нажимаем кнопку "Заказать" в форме заказа')
    def click_form_order_button(self):
        locator = OrderPageLocators.ORDER_ORDER_BUTTON
        self.find_element_with_wait(locator).click()

    @allure.step('Ожидаем отображения модалки "Хотите оформить заказ?"')
    def wait_for_order_confirm_modal(self):
        locator = OrderPageLocators.CONFIRM_ORDER_MODAL
        self.find_element_with_wait(locator)

    @allure.step('Нажимаем кнопку "Да" в модалке "Хотите оформить заказ?"')
    def click_yes_button(self):
        locator = OrderPageLocators.CONFIRM_ORDER_YES_BUTTON
        self.find_element_with_wait(locator).click()

    @allure.step('Подтверждаем заказ в модалке "Хотите оформить заказ?"')
    def confirm_order(self):
        self.wait_for_order_confirm_modal()
        self.click_yes_button()
