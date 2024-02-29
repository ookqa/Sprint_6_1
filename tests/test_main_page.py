import allure
from pages.main_page import MainPage
import pytest
from urls import Urls


class TestMainPageFaq:
    test_data = [
        (1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]

    @allure.title('Проверка секции FAQ')
    @allure.description('На главной странице скроллим к секции "Вопросы о важном", кликаем на вопрос и дожидаемся развернутого блока с ответом')
    @pytest.mark.parametrize("question_number, expected_answer", test_data)
    def test_check_faq_click_item_answer_expand(self, driver, question_number, expected_answer):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        main_page.scroll_and_wait_for_faq_section()
        main_page.click_faq_question_item(question_number)
        main_page.wait_for_faq_answer_item(question_number)
        item_answer = main_page.get_answer_item(question_number)
        assert item_answer == expected_answer
