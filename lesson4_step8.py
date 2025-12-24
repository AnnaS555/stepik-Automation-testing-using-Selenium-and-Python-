from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для расчета математического выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем браузер и переходим на страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, пока цена не станет равной $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Получаем значение x и рассчитываем ответ
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    # Вводим ответ в текстовое поле
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Ждем немного, чтобы увидеть результат
    time.sleep(10)
    # Закрываем браузер
    browser.quit()