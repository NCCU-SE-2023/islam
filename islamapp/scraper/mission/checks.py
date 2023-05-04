from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def _check_elements(driver, verify_element_list):
    for i in range(len(verify_element_list)):
        try:
            driver.find_element(verify_element_list[i]['type'], verify_element_list[i]['value'])
        except:
            return False 
    return True

def check_explore_page(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'div[class="x9f619 xjbqb8w x1lliihq x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'div[class="x9f619 xjbqb8w x1lliihq x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]'}
    ]
    return _check_elements(driver, verify_element_list)

def check_reels_page(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'div[class="x6s0dn4 x78zum5 xieb3on x1ypdohk xdt5ytf"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'div[class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 x78zum5 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd"]'}
    ]
    return _check_elements(driver, verify_element_list)

def check_chat_box(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'button[class="_abl- _abm2"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1y1aw1k x1sxyh0 xwib8y2 xurb0ha x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]'}
    ]
    return _check_elements(driver, verify_element_list)

def check_post_page(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'button[class="_abl- _abm2"]'}
    ]
    return _check_elements(driver, verify_element_list)

def check_alert(driver):
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()
    except:
        pass

def check_profile(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'a[class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye xwhw2v2 x10w6t97 xl56j7k x17ydfre x1f6kntn x1swvt13 x1pi30zi x2b8uid xlyipyv x87ps6o x14atkfc x1n2onr6 x1d5wrs8 x1gjpkn9 x175jnsf xsz8vos x17a9jwe"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'button[class="_abl-"]'}
        ]
    return _check_elements(driver, verify_element_list)


def check_main_page(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'canvas[class="_aarh"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'span[class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1fhwpqd x1s688f x173jzuc x1s3etm8 x676frb x10wh9bi x1wdrske x8viiok x18hxmgj"]'}
    ]
    return _check_elements(driver, verify_element_list)

def check_explore_page(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'div[class="x9f619 xjbqb8w x1lliihq x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'div[class="x9f619 xjbqb8w x1lliihq x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]'}
    ]
    return _check_elements(driver, verify_element_list)

def check_reels_page(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'div[class="x6s0dn4 x78zum5 xieb3on x1ypdohk xdt5ytf"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'div[class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 x78zum5 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd"]'}
    ]
    return _check_elements(driver, verify_element_list)

def check_login_page(driver):
    verify_element_list = [
        {'type':By.CSS_SELECTOR, 'value':'i[style="background-image: url("https://static.cdninstagram.com/rsrc.php/v3/yK/r/ATdtiLb2BQ9.png"); background-position: 0px 0px; background-size: 176px 181px; width: 175px; height: 51px; background-repeat: no-repeat; display: inline-block;"]'}, 
        {'type':By.CSS_SELECTOR, 'value': 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]'}
    ]
    return _check_elements(driver, verify_element_list)