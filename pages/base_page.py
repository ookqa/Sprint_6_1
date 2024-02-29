from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def get_page_title(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "title")))
        return self.driver.title

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):
        return self.driver.current_url

    def send_keys(self, locator):
        element = self.find_element_with_wait(locator)
        element.send_keys()
