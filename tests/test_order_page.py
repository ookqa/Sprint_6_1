import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from urls import Urls


class TestOrderPageOrder:

    @allure.title('Проверка флоу заказа с заполнением всех полей')
    @allure.description(
        'На странице заказа заполняем обязательные и не обязательные поля валидными данными и проверяем успешный заказ. Дата вводится набором.')
    def test_order_all_fields_success(self, driver):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_user_form_title()
        order_page.set_name(Data.TEST_USER_NAME)
        order_page.set_surname(Data.TEST_USER_SURNAME)
        order_page.set_address(Data.TEST_ADDRESS)
        order_page.set_metro_station_by_click()
        order_page.set_phone(Data.TEST_PHONE)
        order_page.click_next_button()
        order_page.wait_for_rent_form_title()
        order_page.set_date_by_keyboard_input(Data.TEST_RENT_DATE)
        order_page.set_rent_period()
        order_page.set_scooter_color()
        order_page.set_comment(Data.RENT_COMMENT)
        order_page.click_form_order_button()
        order_page.confirm_order()
        expect_success_msg_text = order_page.get_order_modal_title()
        assert 'Заказ оформлен' in expect_success_msg_text

    @allure.title('Проверка флоу заказа с заполнением только обязательных полей')
    @allure.description(
        'На странице заказа заполняем только обязательные поля валидными данными и проверяем успешный заказ. Дата выбирается кликом в календаре')
    def test_order_required_fields_success(self, driver):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        main_page.scroll_and_click_home_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_user_form_title()
        order_page.set_name(Data.TEST_USER_NAME)
        order_page.set_surname(Data.TEST_USER_SURNAME)
        order_page.set_address(Data.TEST_ADDRESS)
        order_page.click_metro_station_select()
        order_page.input_metro_station_name(Data.TEST_METRO_STATION_NAME_BEGIN)
        order_page.select_station_from_suggest()
        order_page.set_phone(Data.TEST_PHONE)
        order_page.click_next_button()
        order_page.wait_for_rent_form_title()
        order_page.set_date_from_calendar()
        order_page.set_rent_period()
        order_page.click_form_order_button()
        order_page.confirm_order()
        expect_success_msg_text = order_page.get_order_modal_title()
        assert 'Заказ оформлен' in expect_success_msg_text


class TestOrderPageRedirects:

    @allure.title('Проверка перехода по лого "Яндекс" в хэдере')
    @allure.description('На странице заказа кликаем по лого "Яндекс" проверяем переход на страницу Дзен')
    def test_check_yandex_logo_click(self, driver):
        driver.get(Urls.ORDER_URL)
        order_page = OrderPage(driver)
        order_page.click_header_logo_yandex()
        order_page.switch_to_new_tab()
        current_page_title = order_page.check_title()
        current_url = order_page.get_current_url()
        assert current_page_title == 'Дзен' and current_url == Urls.ZEN_ULR

    @allure.title('Проверка перехода по лого "Самокат" в хэдере')
    @allure.description('На странице заказа кликаем по лого "Самокат" проверяем переход на главную страницу')
    def test_check_scooter_logo_click(self, driver):
        driver.get(Urls.ORDER_URL)
        order_page = OrderPage(driver)
        order_page.click_header_logo_scooter()
        current_page_title = order_page.check_title()
        current_url = order_page.get_current_url()
        assert current_page_title == 'undefined' and current_url == Urls.MAIN_URL
