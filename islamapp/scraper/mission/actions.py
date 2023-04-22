from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scraper.util import log_while_exception
from scraper.mission.checks import *
class VerifyException(Exception):
    pass


@log_while_exception()
def action_login(browser, account, password):
    try:
        # prepare
        account_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        button_xpath = '//*[@id="loginForm"]/div/div[3]'

        # act
        elem_account = WebDriverWait(browser, 600).until(EC.presence_of_element_located((By.XPATH, account_xpath)))
        elem_account.send_keys(account)
        elem_password = WebDriverWait(browser, 600).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
        elem_password.send_keys(password)
        elem_button = WebDriverWait(browser, 600).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
        elem_button.click()

        # verify

    except:
