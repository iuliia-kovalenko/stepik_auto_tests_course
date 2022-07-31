import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

#
def calc():
    return str(math.log(int(time.time())))



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"
                                   ])
def test_the_right_answer(browser, links):
    link_to_open = f"{links}"
    browser.get(link_to_open)
    browser.implicitly_wait(5)
    input_field = browser.find_element_by_class_name("ember-text-area.ember-view.textarea.string-quiz__textarea")
    text_to_enter = str(math.log(int(time.time())))
    # print(text_to_enter)
    input_field.send_keys(text_to_enter)
    click_1 = browser.find_element_by_class_name("submit-submission")
    click_1.click()
    # time.sleep(4)
    if_correct = browser.find_element_by_class_name("smart-hints__hint").text
    assert if_correct == "Correct!"
    print(if_correct)


