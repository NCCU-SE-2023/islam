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
from scraper.instagrapi import Instagrapi
import time
from model.data_models.user_following import UserFollowing


def map_task_type_to_mission(task_type):
    if task_type == TaskType.FOLLOWERS.value:
        return scrape_followers
    elif task_type == TaskType.FOLLOWING.value:
        return scrape_following
    elif task_type == TaskType.LIKES.value:
        return scrape_likes
    elif task_type == TaskType.TEST.value:
        return scrape_test
    elif task_type == TaskType.SECOND.value:
        return scrape_second_step
    else:
        raise Exception("Invalid task type")


@log_while_exception()
def scrape_followers_and_following(driver, task: Task):
    account = task.task_detail["account"]
    password = task.task_detail["password"]
    try:
        # login
        action_login(driver, account, password)
        store_click(driver)
        notification_click(driver)
        time.sleep(2.5)

        go_profile(driver, account)
        time.sleep(2.5)
        user_followers_ids = action_scrape_followers(driver)
        time.sleep(2.5)
        driver.back()
        driver.refresh()

        time.sleep(10)

        go_profile(driver)
        time.sleep(2.5)
        user_followings_ids = action_scrape_following(driver)
        time.sleep(2.5)

        # return data
        follower_number = len(user_followers_ids)
        following_number = len(user_followings_ids)

        raw_data = {
            "scraped_ig_id": account,
            "followers_count": follower_number,
            "followers_list": user_followers_ids,
            "scrape_user": "init_scrape_user",
            "scraped_task_id": "your_task_id",
        }
        UserFollowers.create_user_followers(raw_data)

        raw_data = {
            "scraped_ig_id": account,
            "following_count": following_number,
            "following_list": user_followings_ids,
            "scrape_user": "init_scrape_user",
            "scraped_task_id": "your_task_id",
        }
        UserFollowing.create_user_following(raw_data)
    except Exception as exception:
        raise Exception(exception)


@log_while_exception()
def scrape_followers(driver, task: Task):
    try:
        account = task.task_detail["account"]
        password = task.task_detail["password"]
        task_id = task.task_id

        instagrapi = Instagrapi(account, password, task_id)
        user_followers = instagrapi.get_user_followers(account)
        print(user_followers)
        return user_followers
    except Exception as exception:
        raise Exception(exception)


@log_while_exception()
def scrape_following(driver, task: Task):
    try:
        account = task.task_detail["account"]
        password = task.task_detail["password"]
        task_id = task.task_id

        instagrapi = Instagrapi(account, password, task_id)
        user_following = instagrapi.get_user_following(account)
        print(user_following)
        return user_following
    except Exception as exception:
        raise Exception(exception)


def scrape_likes(driver, task: Task):
    # user_id = task.tasl_i
    account = task.task_detail["account"]
    password = task.task_detail["password"]

    try:
        # login
        get_ig_url(driver)
        time.sleep(2)

        action_login(driver, account, password)
        # # # go to profile page
        time.sleep(2)
        go_profile(driver)
        time.sleep(2)
        # user name
        user_name = driver.find_element(
            By.CSS_SELECTOR,
            'h2[class = "x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]',
        ).text
        # total scrape post number
        post_num = min(
            int(driver.find_element(By.CSS_SELECTOR, 'span[class="_ac2a"]').text), 35
        )
        # click post
        post = 0
        try:
            driver.find_elements(By.CSS_SELECTOR, 'div[class="_aabd _aa8k  _al3l"]')[
                post
            ].click()
        except NoSuchElementException:
            print("click post fail")
        result = {}
        # for i in range(start, post_num):
        index = -1
        while post < post_num:
            post_name = "post{}".format(post + 1)
            # print(post_name)
            result[post_name] = {}
            try:
                # click likes
                try:
                    driver.find_elements(
                        By.CSS_SELECTOR,
                        'span[class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]',
                    )[-1].click()
                except NoSuchElementException:
                    print("click like fail")
                time.sleep(3.5)
                like_account, is_user = scroll_down_likes_window(driver, index)
                # print(is_user)
                # print(like_account)
                result[post_name]["like_number"] = len(like_account)
                result[post_name]["like_list"] = like_account
                time.sleep(0.5)
                esc_likes_window(driver)

            # except NoSuchElementException:
            except IndexError:
                result[post_name]["like_number"] = 0
                result[post_name]["like_list"] = []
            except TimeoutException:
                print("timeout exception")

            if is_user:
                post += 1
                index = -1
            else:
                index = max(index - 1, -10)
                driver.back()
                # print('driver back')
                time.sleep(2)
                driver.find_elements(
                    By.CSS_SELECTOR, 'div[class="_aabd _aa8k  _al3l"]'
                )[post].click()
                continue
            if not to_next_post(driver):
                break
            time.sleep(2)
        raw_data = {
            "scraped_ig_id": user_name,
            "post_like_count": post_num,
            "post_like_dict": result,
            "scrape_user": task.create_user,
            "scraped_task_id": task.task_id,
        }
        print(raw_data)
        return raw_data
    except Exception as exception:
        import traceback

        traceback.print_exc()
        return exception


@log_while_exception()
def scrape_posts(driver, task: Task):
    try:
        pass
    except Exception as exception:
        raise Exception(exception)


def scrape_test(driver, task: Task):
    try:
        driver.get("https://google.com")
        driver.get(
            "https://www.google.com/search?q=asdf&sxsrf=APwXEdep-JbYpd4s50R9vyOzylkYT5Zl8A%3A1683099135644&source=hp&ei=_w1SZKOPJJXXhwPHkYX4Dg&iflsig=AOEireoAAAAAZFIcD0dPHc1BNndp1OqNrM-wKBkEbYTx&ved=0ahUKEwjjiuXw0Nj-AhWV62EKHcdIAe8Q4dUDCAs&uact=5&oq=asdf&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBENEDMg4ILhCABBCxAxDHARDRAzIICC4QgAQQsQMyDgguEIAEELEDEMcBENEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCKBRCxAxCDATIICAAQgAQQsQMyBQgAEIAEOhQILhCABBCxAxCDARDHARDRAxDUAlAAWHhgyAJoAHAAeACAAUyIAc4BkgEBM5gBAKABAQ&sclient=gws-wiz"
        )
        import time

        time.sleep(10)
    except Exception as exception:
        raise Exception(exception)


def scrape_second_step(driver, task):
    try:
        account = task.task_detail["account"]
        password = task.task_detail["password"]
        task_id = task.task_id
        ig_id = task.task_detail["ig_id"]

        user_following = UserFollowing.get_all_user_following_by_ig_id(ig_id).first()

        instagrapi = Instagrapi(account, password, task_id)
        user_following = instagrapi.get_seond_step_followers_and_following(
            user_following
        )
        print(user_following)
        return {}
    except Exception as exception:
        raise Exception(exception)
