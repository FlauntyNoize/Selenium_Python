import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_form1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Giorno")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Giovanna")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("ihaveadream@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "String should be equal")
    
    def test_form2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Giorno")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Giovanna")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("ihaveadream@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "String should be equal")

if __name__ == "__main__":
    unittest.main()