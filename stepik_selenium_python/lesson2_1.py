from selenium import webdriver

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
# x = input()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
print(x)
y = calc(x)
input_field_y = browser.find_element_by_id("answer")
input_field_y.send_keys(y)
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
option2 = browser.find_element_by_css_selector("[value='robots']")
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()