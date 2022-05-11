import os
from selenium import webdriver


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

element_1 = browser.find_element_by_name('firstname')
element_1.send_keys("test")
element_2 = browser.find_element_by_name('lastname')
element_2.send_keys("test")
element_3 = browser.find_element_by_name('email')
element_3.send_keys("test")


file_name = "test.txt"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, file_name)           # добавляем к этому пути имя файла
element = browser.find_element_by_id("file")

element.send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn")
button.click()