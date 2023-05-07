from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CDM

class Driver(object):
    """Congigure and return a selenium webdriver instance.
    :param hub_endpoint: (optional) the endpoint of the selenium hub. If None, the driver will start locally.
    """
    def __init__(self, hub_endpoint=None):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument('--no-sandbox')
        if hub_endpoint:
            self.is_remote = True
            self.driver = webdriver.Remote(hub_endpoint, options=self.options)
        else:
            self.is_remote = False
            self.driver = webdriver.Chrome(CDM().install(), options=self.options)

    def __del__(self):
        self.driver.quit()

