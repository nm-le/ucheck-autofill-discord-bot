"""
Automate UCheck
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
import time

date = datetime.now().strftime('%Y%m%d')


def automate_ucheck(utorid: str, pwd: str) -> None:
    """
    Autofill UCheck form.
    :param utorid: passed in from discord_bot.py
    :param pwd: passed in from discord_bot.py
    :return: None
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://ucheck.utoronto.ca/')
    wait = WebDriverWait(driver, 100)

    # enter utorid
    username = driver.find_element(By.ID, "username")
    username.send_keys(utorid)

    # enter password
    password = driver.find_element(By.ID, "password")
    password.send_keys(pwd)

    # submit login info
    driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/form/button').click()

    # start form
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/button'))).click()

    all_buttons = [
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[6]'   # fully vaxxed
        '/div/div/div/div/div/div/div/div/fieldset/label[2]',
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[8]'   # symptoms
        '/div/div/div/div/div/div/div/div/fieldset/label[1]',
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[10]'  # symptoms 2
        '/div/div/div/div/div/div/div/div/fieldset/label[1]',
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[12]'  # travelled in 14
        '/div/div/div/div/div/div/div/div/fieldset/label[1]',
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[14]'  # isolating
        '/div/div/div/div/div/div/div/div/fieldset/label[1]',
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[16]'  # close contact
        '/div/div/div/div/div/div/div/div/fieldset/label[1]',
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[18]'  # exposure
        '/div/div/div/div/div/div/div/div/fieldset/label[1]',
        '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[20]'  # test kit
        '/div/div/div/div/div/div/div/div/fieldset/label[1]',
    ]

    def click_all(xpath) -> None:
        """Clicks lol"""
        element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, xpath)
            )
        )
        driver.execute_script("arguments[0].click();", element)

    for button in all_buttons:
        click_all(button)

    # submit form
    wait.until(EC.element_to_be_clickable
               ((By.XPATH,
                 '/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/div/button'))).click()

    time.sleep(4)

    path = 'screenshots/' + date + utorid + '.png'

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div').screenshot(path)