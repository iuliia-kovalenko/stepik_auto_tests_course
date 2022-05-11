from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

num1 = browser.find_element_by_id("input_value")
x = num1.text
y = str(math.log(abs(12 * math.sin(int(x)))))
input_field_y = browser.find_element_by_id("answer")
input_field_y.send_keys(y)
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()