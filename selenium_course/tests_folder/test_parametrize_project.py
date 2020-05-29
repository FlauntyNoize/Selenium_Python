from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math


@pytest.fixture(scope = "function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1", 
    "https://stepik.org/lesson/236896/step/1", 
    "https://stepik.org/lesson/236897/step/1", 
    "https://stepik.org/lesson/236898/step/1", 
    "https://stepik.org/lesson/236899/step/1", 
    "https://stepik.org/lesson/236903/step/1", 
    "https://stepik.org/lesson/236904/step/1", 
    "https://stepik.org/lesson/236905/step/1"])

def test_links(browser, link):
    link = f"{link}"
    browser.get(link)
    browser.implicitly_wait(5)

    result = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "textarea"))
    )
    answer = math.log(int(time.time()))
    result.send_keys(str(answer))

    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    feedback = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    assert feedback.text == "Correct!", "Feedback error - wrong result!"