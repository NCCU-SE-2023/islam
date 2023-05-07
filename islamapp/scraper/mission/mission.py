# A mission is a funcion that takes a webdriver as 
# input then use that webdriver to do a series of 
# actions finally return a result.
# ========================================================
# A mission should able to start no matter what page the webdriver is on.

from model.task import Task
from scraper.mission.actions import *
from scraper.mission.checks import *
from model.data_models.user_followers import *
from model.data_models.user_following import *
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
        # scrape followers
        go_profile(driver)
        user_followers_ids=scrape_follower(driver)
        
        # scrape following
        go_profile(driver)
        user_followings_ids=scrape_following(driver)
        
        # return data
        for user_followers_id in user_followers_ids:
            raw_data = {
                "scraped_ig_id": "your_ig_id",
                "followers_count": 100,  # 先假設每人追蹤者數量為100 目前抓follower & following跑到一半都會斷掉
                "followers_list": ["follower1", "follower2", "follower3"],  # 假設追蹤者列表
                "scrape_user": "your_scrape_user", #發起ISLAM者
                "scraped_task_id": "your_task_id" 
            }
            UserFollowers.create_user_followers(raw_data)
        
        for user_following_id in user_following_ids:
            raw_data = {
                "scraped_ig_id": user_id,
                "following_count": 0,  
                "following_list": [],  
                "scrape_user": "your_scrape_user",
                "scraped_task_id": "your_scraped_task_id"
            }
            UserFollowing.create_user_following(raw_data)
        
        
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
        # login
        action_login(driver, account, password)
        store_click(driver)
        notification_click(driver)
        
        # go to profile page
        go_profile(driver)
        time.sleep(2)

        # total scrape post number
        post_num = min(int(driver.find_element(By.CSS_SELECTOR, 'span[class="_ac2a"]').text), 35)
        # click first post
        driver.find_elements(By.CSS_SELECTOR, 'div[class="_aabd _aa8k  _al3l"]')[0].click()
        result = {}
        for i in range(post_num):
            post_name = 'post{}'.format(i+1)
            result[post_name] = {}
            try:
                # click likes
                driver.find_elements(By.CSS_SELECTOR, 'span[class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')[-1].click()
                time.sleep(4)
                like_account = scroll_down_likes_window(driver)

                result[post_name]["like_number"] = len(like_account)
                result[post_name]["like_list"] = like_account
                time.sleep(0.5)
                esc_likes_window(driver)

            except IndexError:
                result[post_name]["like_number"] = 0
                result[post_name]["like_list"] = []
            except TimeoutException:
                print('{}: timeout exception'.format(post_name))

            if not to_next_post(driver):
                break
            time.sleep(2)
    except Exception as exception:
        raise Exception(exception)

@log_while_exception()
def scrape_posts(driver, task:Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)
