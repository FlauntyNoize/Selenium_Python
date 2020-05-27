from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.implicitly_wait(5)

    book_button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book_button.click()

    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    result = browser.find_element_by_id("answer")
    result.send_keys(y)

    button.click()

finally:
    time.sleep(10)
    browser.quit()
