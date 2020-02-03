from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button_book = browser.find_element_by_id("book")
    button_book.click()
    x_string = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_string)
    x = int(x_string.text)
    y = calc(x)
    y_str = str(y)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y_str)
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
