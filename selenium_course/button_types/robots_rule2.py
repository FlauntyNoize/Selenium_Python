from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    
    result = browser.find_element_by_id("answer")
    result.send_keys(y)

    robo_check = browser.find_element_by_id("robotCheckbox")
    robo_check.click()

    robo_radio = browser.find_element_by_id("robotsRule")
    robo_radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла