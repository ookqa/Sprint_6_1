from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")
    HEADER_LOGO_SCOOTER = (By.XPATH, "//a[@href='/' and contains(@class, 'Header_LogoScooter')]")
    HOME_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button")
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']")
    FAQ_QUESTION_ITEMS = {
        1: [By.XPATH, "//div[@id='accordion__heading-0']/parent::div"],
        2: [By.XPATH, "//div[@id='accordion__heading-1']/parent::div"],
        3: [By.XPATH, "//div[@id='accordion__heading-2']/parent::div"],
        4: [By.XPATH, "//div[@id='accordion__heading-3']/parent::div"],
        5: [By.XPATH, "//div[@id='accordion__heading-4']/parent::div"],
        6: [By.XPATH, "//div[@id='accordion__heading-5']/parent::div"],
        7: [By.XPATH, "//div[@id='accordion__heading-6']/parent::div"],
        8: [By.XPATH, "//div[@id='accordion__heading-7']/parent::div"]
    }

    FAQ_ANSWER_ITEMS = {
        1: (By.XPATH, "//div[@id='accordion__panel-0']"),
        2: (By.XPATH, "//div[@id='accordion__panel-1']"),
        3: (By.XPATH, "//div[@id='accordion__panel-2']"),
        4: (By.XPATH, "//div[@id='accordion__panel-3']"),
        5: (By.XPATH, "//div[@id='accordion__panel-4']"),
        6: (By.XPATH, "//div[@id='accordion__panel-5']"),
        7: (By.XPATH, "//div[@id='accordion__panel-6']"),
        8: (By.XPATH, "//div[@id='accordion__panel-7']")
    }
