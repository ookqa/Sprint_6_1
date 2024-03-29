from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_USER_FORM_TITLE = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    ORDER_RENT_FORM_TITLE = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    ORDER_NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_STATION_CONTROL = (By.XPATH, "//div[@class='select-search']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_DROPDOWN = (By.XPATH, "//div[@class='select-search__select']")
    METRO_STATION_ITEM = (By.XPATH, "//ul[@class='select-search__options']//div[text()='Сокольники']")
    METRO_STATION_SUGGEST = (By.XPATH, "//ul[@class='select-search__options']//div[text()='Охотный Ряд']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_POPUP = (By.XPATH, "//div[@class='react-datepicker-popper']")
    CALENDAR_TEST_ITEM = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@aria-label, '2-е марта')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    RENT_PERIOD_CONTROL = (By.XPATH, "//div[@class='Dropdown-root']")
    RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-menu']")
    RENT_PERIOD_DROPDOWN_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    COLOR_OPTION = (By.XPATH, "//input[@id='black']")
    CONFIRM_ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]/parent::div[contains(@class, 'Order_Content')]")
    CONFIRM_ORDER_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    CONFIRM_ORDER_SUCCESS_MSG_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
    HEADER_LOGO_SCOOTER = (By.XPATH, "//a[@href='/' and contains(@class, 'Header_LogoScooter')]")
    HEADER_LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru' and contains(@class, 'Header_LogoYandex')]")
