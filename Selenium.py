import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"C:\\chromedriver_win32\\chromedriver.exe")
# заходим на почту
driver.get("https://mail.ru/")

# находим кнопку логина и нажимаем на нее
btn_blue = driver.find_element_by_xpath('//*[@id="mailbox:submit"]/input')
btn_blue.click()

# Убеждаемся, что не вошли
try:
    btn_blue = driver.find_element_by_xpath('//*[@id="mailbox:submit"]/input')
    print("Вы не вошли!")
except NoSuchElementException:
    print("Вы вошли!")

    # Вводим логин
    input_em = driver.find_element_by_xpath('mailbox_login')
    input_em.send_keys('yaroslav.selenium@mail.ru')
    btn_blue.click()

# Убеждаемся, что не вошли
try:
    btn_blue = driver.find_element_by_xpath('//*[@id="mailbox:submit"]/input')
    print("Вы не вошли!")
except NoSuchElementException:
    print("Вы вошли!")
# Вводим неверный пароль и пытаемся войти

input_pass = driver.find_element_by_xpath('//*[@id="mailbox:submit"]/input')
input_pass.send_keys('qwerty')
btn_blue.click()

# Убеждаемся что на другой странице
wait_for_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, (('//*[@id="mailbox:submit"]/input')))
))
if driver.current_url == "https://mail.ru/":
    print("Вы не сменили страницу!")
else:
    print("Вы сменили страницу!")

# Проверяем, на странице ошибки ли мы
try:
    log_mes_btn = driver.find_element_by_xpath('login_message')
    print("Вы на странице ошибки!")
except NoSuchElementException:
    print("Вы вошли?")

    # ищем кнопку регистрации и нажимаем
    btn_blue = driver.find_element_by_xpath('login_reg_button')
    btn_blue.click()

    # Убеждаемся, что мы вновь на первой странице
    wait_for_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "ij_submit"))
    )

    if driver.current_url == "https://mail.ru/":
        print("Вы на первой странице!")
    elif driver.current_url == "https://mail.ru/join":
        print("Вы не на первой странице, но на ее аналоге.")
    else:
        print("Вы не на первой странице!")