"""
Automate UCheck
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        
import time

def verify_login(utorid: str, pwd: str) -> bool:
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

    time.sleep(4)
    def check_exists_by_xpath(xpath):
        try:
            driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True
    
    return check_exists_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/button')