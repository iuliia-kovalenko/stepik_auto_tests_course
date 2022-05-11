from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

num1 = browser.find_element_by_id("input_value")
x = num1.text
y = str(math.log(abs(12 * math.sin(int(x)))))
input_field_y = browser.find_element_by_id("answer")
input_field_y.send_keys(y)
browser.execute_script("window.scrollBy(0, 100);")

option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()
option2 = browser.find_element_by_css_selector("[id='robotsRule']")
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()
