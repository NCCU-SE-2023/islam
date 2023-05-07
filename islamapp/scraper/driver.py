from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CDM

class Driver(object):
    """Congigure and return a selenium webdriver instance.
    """
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('window-size=1920x1080')
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(CDM.install(), options = self.options)
    def __delete__(self):
        self.driver.quit()

