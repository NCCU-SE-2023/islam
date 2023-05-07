# A mission is a funcion that takes a webdriver as 
# input then use that webdriver to do a series of 
# actions finally return a result.
# ========================================================
# A mission should able to start no matter what page the webdriver is on.


from scraper.mission.actions import *
from scraper.mission.checks import *
from model.data_models.user_followers import *
from model.data_models.user_following import *
from model.data_models.user_post_like import *
from model.task import Task, TaskType
from scraper.util import log_while_exception
import time

def map_task_type_to_mission(task_type):
    if task_type == TaskType.FOLLOWERS.value:
        return scrape_followers_and_following
    elif task_type == TaskType.FOLLOWING.value:
        return scrape_followers_and_following
    elif task_type == TaskType.LIKES.value:
        return scrape_likes
    elif task_type == TaskType.TEST.value:
        return scrape_test
    else:
        raise Exception("Invalid task type")

@log_while_exception()
def scrape_followers_and_following(driver, task:Task):    
    try:
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
    # user_id = task.tasl_i
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
        # user name
        user_name = driver.find_element(By.CSS_SELECTOR, 'h2[class = "x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]').text
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
        raw_data = {
                "scraped_ig_id": user_name,
                "post_like_count": post_num,  
                "post_like_dict": result,  
                "scrape_user": "your_scrape_user",
                "scraped_task_id": "your_scraped_task_id"
            }
        return raw_data

    except Exception as exception:
        return exception

@log_while_exception()
def scrape_posts(driver, task:Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)

def scrape_test( driver, task:Task):
    try:
        driver.get("https://google.com")
        driver.get("https://www.google.com/search?q=asdf&sxsrf=APwXEdep-JbYpd4s50R9vyOzylkYT5Zl8A%3A1683099135644&source=hp&ei=_w1SZKOPJJXXhwPHkYX4Dg&iflsig=AOEireoAAAAAZFIcD0dPHc1BNndp1OqNrM-wKBkEbYTx&ved=0ahUKEwjjiuXw0Nj-AhWV62EKHcdIAe8Q4dUDCAs&uact=5&oq=asdf&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBENEDMg4ILhCABBCxAxDHARDRAzIICC4QgAQQsQMyDgguEIAEELEDEMcBENEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCKBRCxAxCDATIICAAQgAQQsQMyBQgAEIAEOhQILhCABBCxAxCDARDHARDRAxDUAlAAWHhgyAJoAHAAeACAAUyIAc4BkgEBM5gBAKABAQ&sclient=gws-wiz")
        import time
        time.sleep(10)
    except Exception as exception:
        raise Exception(exception)