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



def get_ig_url(driver):
    login_url = 'https://www.instagram.com/'
    driver.get(login_url)
def action_login(driver, account, password):
    try:
        # prepare
        account_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        button_xpath = '//*[@id="loginForm"]/div/div[3]'
        # act
        try:
            elem_account = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, account_xpath)))
            elem_account.send_keys(account)
            time.sleep(1)
            elem_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
            elem_password.send_keys(password)
            time.sleep(2)
            elem_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
            elem_button.click()
            elem_button.click()
            print("input account and password success")
        except:
            print("input account and password fail")

        try:
            alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 x972fbf xcfux6l x1qhh985 xm0m39n xm3z3ea x1x8b98j x131883w x16mih1h xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xjbqb8w x1n5bzlp x173jzuc x1yc6y37"]')))
            time.sleep(2)
            alert.click()
        except TimeoutException:
            print('no alert 1')        
        time.sleep(2)
        try:
            driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]').click()  
        except NoSuchElementException:
            print('no alert 2')

        if check_main_page(driver):
            print('login success')
        else:
            print('login fail1')
    except:
        print('login fail2')
@log_while_exception()
def store_click(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 x972fbf xcfux6l x1qhh985 xm0m39n xm3z3ea x1x8b98j x131883w x16mih1h xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xjbqb8w x1n5bzlp x173jzuc x1yc6y37"]'))).click()
    except:
        print('store click fail')

@log_while_exception()        
def notification_click(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]'))).click()  
    except:
        print('notification click fail')

def go_profile(driver):
    if not check_profile(driver):
        try:
            driver.find_element(By.CSS_SELECTOR, 'span[class="xnz67gz x14yjl9h xudhj91 x18nykt9 xww2gxu x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 x1ykvv32 xougopr x159fomc xnp5s1o x194ut8o x1vzenxt xd7ygy7 xt298gk x1xrz1ek x1s928wv x162n7g1 x2q1x1w x1j6awrg x1n449xj x1m1drc7"]').click()
        except NoSuchElementException:
            if check_post_page(driver):
                close_post_page(driver)
        time.sleep(5)
        if check_profile(driver):
            print("go to profile success1")
        else:
            print("go to profile fail")
    else:
        print("go to profile success2")  

   
@log_while_exception()       
def action_scrape_followers(driver):
    followers_accounts = []
    try:
        followers_id = "followers"
        driver.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % followers_id)).click()
        
        time.sleep(2)

        repeat = 0
        followers_area = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: auto; overflow: hidden auto;"]'))).find_element(By.TAG_NAME, 'div')
        while True:
            accounts = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")
            
            for account in accounts:
                source_text = account.text
                followers_account = source_text.split('\n')[0]
                if followers_account not in followers_accounts:
                    followers_accounts.append(followers_account)
            #print(followers_accounts)
            click_to_scroll = followers_area.find_elements(By.CSS_SELECTOR, 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"]')[-1]
            click_to_scroll.click()
            time.sleep(1)

            new_click_to_scroll = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")[-1]
            if new_click_to_scroll == click_to_scroll:
                repeat += 1
                if repeat == 2:
                    break
        return followers_accounts
        
    except:
        pass
@log_while_exception()       
def action_scrape_following(driver):
    following_accounts = []
    try:
        following_id = "following"
        driver.find_element(
            By.CSS_SELECTOR, ("a[href*=%s]" % following_id)).click()
        
        time.sleep(2)

        repeat = 0
        following_area = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: auto; overflow: hidden auto;"]'))).find_element(By.TAG_NAME, 'div')
        while True:
            accounts = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")
            
            for account in accounts:
                source_text = account.text
                following_account = source_text.split('\n')[0]
                if following_account not in following_accounts:
                    following_accounts.append(following_account)
            
            click_to_scroll = following_area.find_elements(By.CSS_SELECTOR, 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"]')[-1]
            click_to_scroll.click()
            time.sleep(1)

            new_click_to_scroll = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")[-1]
            if new_click_to_scroll == click_to_scroll:
                repeat += 1
                if repeat == 2:
                    break
          
        return following_accounts
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
        count=1
        while True:
            try:
                element = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[aria-label='下一步']"))).click()
                count=count+1
            except TimeoutException:
                break
        driver.back()
        print(count)
        driver.refresh()
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//div[contains(@class,'_aagu')]").click()
        time.sleep(2)
        
        tagged_names = []
        for i in range(count-1):
            elements = driver.find_elements(By.CSS_SELECTOR,'a.x1i10hfl')  


            for index, element in enumerate(elements):
                name = element.text  
                if index == len(elements) - 2:
                    tagged_names.append(name)  
            
            
            driver.find_element(
            By.CSS_SELECTOR, "[aria-label='下一步']").click()
            time.sleep(2)
        time.sleep(2)
        elements = driver.find_elements(By.CSS_SELECTOR,'a.x1i10hfl')  


        for index, element in enumerate(elements):
            name = element.text  
            if index == len(elements) - 2:
                tagged_names.append(name)  
        return tagged_names 
    except:
        print("tagged post fail")
        pass
    
@log_while_exception() 
def scroll_down_likes_window(driver, index):
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
            click_to_scroll = like_area.find_elements(By.CSS_SELECTOR, 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]')[index]
            click_to_scroll.click()
            time.sleep(1)

            new_click_to_scroll = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")[index]
            if new_click_to_scroll == click_to_scroll:
                repeat += 1
                if repeat == 2:
                    break
    except:
        print('Scroll down failed')
    try:
        driver.find_element(By.CSS_SELECTOR, 'h2[class = "x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')
        return likes_accounts, True
    except NoSuchElementException:
        return likes_accounts, False

@log_while_exception() 
def to_next_post(driver):
    try:
        next_list = ['svg[aria-label="Next"]','svg[aria-label="下一步"]' ]
        for next in next_list:
            try:
                driver.find_element(By.CSS_SELECTOR, next).click()
                break
            except NoSuchElementException:
                pass
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

        print('login fail')
    
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
