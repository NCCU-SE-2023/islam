# A mission is a funcion that takes a webdriver as 
# input then use that webdriver to do a series of 
# actions finally return a result.
# ========================================================
# A mission should able to start no matter what page the webdriver is on.

from model.task import Task
from scraper.util import log_while_exception

@log_while_exception()
def scrape_followers_and_following(driver, task:Task):
    try:
        
        # login
        username_input = browser.find_element('name', 'username')
        password_input = browser.find_element('name', 'password')

        username_input.send_keys(account)
        password_input.send_keys(password)

        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
        login_click = browser.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button/div')
        login_click.click()

        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
        store_click = browser.find_elements(
            "xpath", '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')[0]
        store_click.click()

        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
        notification_click = browser.find_elements(
            "xpath", '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')[0]
        notification_click.click()
        
        # go to profile page
        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a/div')))
        profile_click = browser.find_elements(
            "xpath", '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a/div')[0]
        profile_click.click()

        time.sleep(3)
        
       
        # scrape followers
        follower_id = "follower"
        browser.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % follower_id)).click()

        time.sleep(2)

        scroll_box = browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        time.sleep(5)

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht

            ht = browser.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)

        links = scroll_box.find_elements(
            By.TAG_NAME, 'a')
        time.sleep(2)
        follower_names = [name.text for name in links if name.text != '']

        browser.back()
        
        # scrape following
        following_id = "following"
        browser.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % following_id)).click()
        time.sleep(2)

        scroll_box = browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        time.sleep(5)

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht

            ht = browser.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)

        links = scroll_box.find_elements(
            By.TAG_NAME, 'a')
        time.sleep(2)
        following_names = [name.text for name in links if name.text != '']
        
        # return data
       result=following_names+follower_names
       return result
    
        pass
    except Exception as exception:
        raise Exception(exception)

@log_while_exception()
def scrape_followers(driver, task:Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)

@log_while_exception()
def scrape_following(driver, task:Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)

@log_while_exception()
def scrape_likes(driver, task:Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)

@log_while_exception()
def scrape_posts(driver, task:Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)
