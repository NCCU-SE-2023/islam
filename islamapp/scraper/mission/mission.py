# A mission is a funcion that takes a webdriver as 
# input then use that webdriver to do a series of 
# actions finally return a result.
# ========================================================
# A mission should able to start no matter what page the webdriver is on.

from model.task import Task
from scraper.mission.actions import *
from scraper.mission.checks import *
from scraper.util import log_while_exception
import time

@log_while_exception()
def scrape_followers_and_following(driver, task:Task):
    account = task.task_detail['account']
    password = task.task_detail['password']
    try:
        # login
        action_login(driver, account, password)
        store_click(driver)
        notification_click(driver)
        
        # go to profile page
        go_profile(driver)
        
        # scrape followers
        follower_list=scrape_follower(driver)
        
        # scrape following
        following_list=scrape_following(driver)
        
        # return data
        # ...
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
    account = task.task_detail['account']
    password = task.task_detail['password']

    try:
        if check_login_page:
            action_login(driver, account, password)
            store_click(driver)
            notification_click(driver)
            time.sleep(2)
        go_profile()
        time.sleep(2)
        # total post number
        post_num = min(int(driver.find_element(By.CSS_SELECTOR, 'span[class="_ac2a"]').text), 35)
        # click first post
        driver.find_element(By.CSS_SELECTOR, 'div[class="_aabd _aa8k  _al3l"]').click()

        for i in range(post_num):
            print('post {}'.format(i+1))
            try:
                # click likes
                time.sleep(1)
                driver.find_elements(By.CSS_SELECTOR, 'span[class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')[-1].click()
                time.sleep(4)
                like_account = scroll_down_likes_window(driver)
                print(len(like_account))
                time.sleep(0.5)
                esc_likes_window(driver)
            except (NoSuchElementException, IndexError):
                print('no one like this page')
            except TimeoutException:
                print('timeout exception')

            if not to_next_post(driver):
                break
            time.sleep(1)
        close_post_page(driver)
    except Exception as exception:
        raise Exception(exception)

@log_while_exception()
def scrape_posts(driver, task:Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)
