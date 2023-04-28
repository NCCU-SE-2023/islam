from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scraper.util import log_while_exception
from scraper.mission.checks import *
class VerifyException(Exception):
    pass


@log_while_exception()
def action_login(driver, account, password):
    try:
        # prepare
        account_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        button_xpath = '//*[@id="loginForm"]/div/div[3]'

        # act
        elem_account = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, account_xpath)))
        elem_account.send_keys(account)
        elem_password = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
        elem_password.send_keys(password)
        elem_button = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
        elem_button.click()

        # verify

    except:
        
@log_while_exception()
def store_click(driver):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
        store_click = driver.find_elements(
            By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')[0]
        store_click.click()
        
    except:
        
@log_while_exception()        
def notification_click(driver):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
        notification_click = driver.find_elements(
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')[0]
        notification_click.click()
        
    except:
        
@log_while_exception()       
def go_profile(driver):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a/div')))
        go_profile = driver.find_elements(
            By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a/div')[0]
        go_profile.click()
        
    except:
        
@log_while_exception()       
def scrape_follower(driver):
    try:
        follower_id = "follower"
        driver.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % follower_id)).click()

        scroll_box = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht

            ht = driver.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)

        links = scroll_box.find_elements(
            By.TAG_NAME, 'a')
        
        follower_names = [name.text for name in links if name.text != '']
        return follower_names
        
    except:
        
@log_while_exception()       
def scrape_following(driver):
    try:
        following_id = "following"
        driver.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % following_id)).click()

        scroll_box = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht

            ht = driver.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)

        links = scroll_box.find_elements(
            By.TAG_NAME, 'a')
        
        following_names = [name.text for name in links if name.text != '']
        return following_names
        
        
    except:
        
