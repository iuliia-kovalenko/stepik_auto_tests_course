from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
chest_search = browser.find_element_by_id("treasure")
get_value_attribute = chest_search.get_attribute("valuex")

x = get_value_attribute
print(x)
y = calc(x)
input_field_y = browser.find_element_by_id("answer")
input_field_y.send_keys(y)
option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()
option2 = browser.find_element_by_css_selector("[id='robotsRule']")
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()
