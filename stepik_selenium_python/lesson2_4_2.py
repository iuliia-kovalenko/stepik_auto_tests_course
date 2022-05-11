from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
# button.click()
button1 = browser.find_element_by_css_selector("button.btn.btn-primary")
button1.click()

browser.execute_script("window.scrollBy(0, 100);")
num1 = browser.find_element_by_id("input_value")
x = num1.text
y = str(math.log(abs(12 * math.sin(int(x)))))
input_field_y = browser.find_element_by_id("answer")
input_field_y.send_keys(y)
button2 = browser.find_element_by_css_selector("button[id='solve']")
button2.click()