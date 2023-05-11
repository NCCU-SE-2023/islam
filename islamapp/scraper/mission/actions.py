from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from scraper.util import log_while_exception
from scraper.mission.checks import *
import time

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
        print('login fail')
@log_while_exception()
def store_click(driver):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 x972fbf xcfux6l x1qhh985 xm0m39n xm3z3ea x1x8b98j x131883w x16mih1h xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xjbqb8w x1n5bzlp x173jzuc x1yc6y37"]'))).click()
    except:
        print('store click fail')

@log_while_exception()        
def notification_click(driver):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]'))).click()  
    except:
        print('notification click fail')

@log_while_exception()       
def go_profile(driver , ig_id):
    while not check_profile(driver):
        try:
            profile_url = 'https://www.instagram.com/'+ig_id+"/"
            driver.get(profile_url)
            break
        except:
            print('go profile fail')  

   
@log_while_exception()       
def scrape_follower(driver):
    try:
        follower_id = "follower"
        driver.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % follower_id)).click()
        
        time.sleep(2)
        
        scroll_box = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        
        time.sleep(2)
        
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
        pass
@log_while_exception()       
def scrape_following(driver):
    try:
        following_id = "following"
        driver.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % following_id)).click()
        
        time.sleep(2)
        
        scroll_box = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        
        time.sleep(2)
        
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
        pass
    
@log_while_exception()       
def tagged_post(driver):
    try:
        id = "tagged"
        driver.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % id)).click()

        time.sleep(2)

        driver.find_element(
            By.XPATH, "//div[contains(@class,'_aagu')]").click()
        time.sleep(2)

        wait = WebDriverWait(driver, 10)
        while True:
            # grab the data

            # click next link
            try:
                element = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[aria-label='下一步']"))).click()
            except TimeoutException:
                break
    except:
        pass
    
@log_while_exception() 
def scroll_down_likes_window(driver):
    likes_accounts = []
    try:
        repeat = 0
        like_area = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 356px; overflow: hidden auto;"]'))).find_element(By.TAG_NAME, 'div')
        while True:
            accounts = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
            
            for account in accounts:
                source_text = account.text
                follower_account = source_text.split('\n')[0]
                if follower_account not in likes_accounts:
                    likes_accounts.append(follower_account)
            click_to_scroll = like_area.find_elements(By.CSS_SELECTOR, 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]')[-1]
            click_to_scroll.click()
            time.sleep(1)

            new_click_to_scroll = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")[-1]
            if new_click_to_scroll == click_to_scroll:
                repeat += 1
                if repeat == 2:
                    break
    except:
        print('Scroll down failed')
    return likes_accounts

@log_while_exception() 
def to_next_post(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="下一步"]').click()
    except NoSuchElementException:
        print('No other post')
        return False
    return True

@log_while_exception() 
def esc_likes_window(driver):
    try:
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        print('Press ESC failed')

@log_while_exception() 
def close_post_page(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="關閉"]').click()
    except:
        pass
    
# @log_while_exception() 
# def scrape_like(driver):
#     try:
#         # total post number
#         post_num = min(int(driver.find_element(By.CSS_SELECTOR, 'span[class="_ac2a"]').text), 35)
#         # click first post
#         driver.find_element(By.CSS_SELECTOR, 'div[class="_aabd _aa8k  _al3l"]').click()

#         for i in range(post_num):
#             print('post {}'.format(i+1))
#             try:
#                 # click likes
#                 time.sleep(1)
#                 driver.find_elements(By.CSS_SELECTOR, 'span[class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')[-1].click()
#                 time.sleep(4)
#                 like_account = scroll_down_likes_window(driver)
#                 print(len(like_account))
#                 time.sleep(0.5)
#                 esc_likes_window(driver)
#             except (NoSuchElementException, IndexError):
#                 print('no one like this page')
#             except TimeoutException:
#                 print('timeout exception')

#             if not to_next_post(driver):
#                 break
#             time.sleep(1)
#         close_post_page(driver)
#     except:
#         pass
