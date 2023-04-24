from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CDM

class Driver(object):
    """Congigure and return a selenium webdriver instance.
    """
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(CDM.install(), options = self.options)
    def __delete__(self):
        self.driver.quit()

