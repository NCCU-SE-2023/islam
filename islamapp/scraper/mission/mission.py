# A mission is a funcion that takes a webdriver as 
# input then use that webdriver to do a series of 
# actions finally return a result.
# ========================================================
# A mission should able to start no matter what page the webdriver is on.

from model.task import Task, TaskType
from scraper.util import log_while_exception

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
        # login
        # go to profile page
        # scrape followers
        # scrape following
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

def scrape_test( driver, task:Task):
    try:
        driver.get("https://google.com")
        driver.get("https://www.google.com/search?q=asdf&sxsrf=APwXEdep-JbYpd4s50R9vyOzylkYT5Zl8A%3A1683099135644&source=hp&ei=_w1SZKOPJJXXhwPHkYX4Dg&iflsig=AOEireoAAAAAZFIcD0dPHc1BNndp1OqNrM-wKBkEbYTx&ved=0ahUKEwjjiuXw0Nj-AhWV62EKHcdIAe8Q4dUDCAs&uact=5&oq=asdf&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBENEDMg4ILhCABBCxAxDHARDRAzIICC4QgAQQsQMyDgguEIAEELEDEMcBENEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCKBRCxAxCDATIICAAQgAQQsQMyBQgAEIAEOhQILhCABBCxAxCDARDHARDRAxDUAlAAWHhgyAJoAHAAeACAAUyIAc4BkgEBM5gBAKABAQ&sclient=gws-wiz")
        import time
        time.sleep(10)
    except Exception as exception:
        raise Exception(exception)