import allure
import pytest
from locators.main_page_locators import QALocators
from pages.main_page import MainPage
from data import AnswerText, Urls

class TestAQ:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (QALocators.QUESTION_1, QALocators.ANSWER_1, AnswerText.ANSWER_TEXT_1),
        (QALocators.QUESTION_2, QALocators.ANSWER_2, AnswerText.ANSWER_TEXT_2),
        (QALocators.QUESTION_3, QALocators.ANSWER_3, AnswerText.ANSWER_TEXT_3),
        (QALocators.QUESTION_4, QALocators.ANSWER_4, AnswerText.ANSWER_TEXT_4),
        (QALocators.QUESTION_5, QALocators.ANSWER_5, AnswerText.ANSWER_TEXT_5),
        (QALocators.QUESTION_6, QALocators.ANSWER_6, AnswerText.ANSWER_TEXT_6),
        (QALocators.QUESTION_7, QALocators.ANSWER_7, AnswerText.ANSWER_TEXT_7),
        (QALocators.QUESTION_8, QALocators.ANSWER_8, AnswerText.ANSWER_TEXT_8)
    ])
    @allure.description("Проверка ответа на вопрос.")
    def test_question_and_answer(self, driver, question_locator, answer_locator, expected_text):
        faq_page = MainPage(driver)
        faq_page.open_page(Urls.MAIN_PAGE)
        actual_text = faq_page.click_question_and_get_answer_text(question_locator, answer_locator)
        assert actual_text == expected_text, f"Текст на странице не соответствует ожидаемому: {expected_text}"
