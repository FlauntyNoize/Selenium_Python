from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Giorno")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Giovanna")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ihaveadream@gmail.com")

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла     
    file_path = os.path.join(current_dir, 'empty_file.txt')           

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла