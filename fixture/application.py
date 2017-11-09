#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.james import JamesHelper
from fixture.project import ProjectHelper

class Application:
    #def __init__(self, browser = "firefox"):
    def __init__(self, browser, config):
                #self.wd = WebDriver(capabilities={"marionette": False})
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
            #self.wd.implicitly_wait(5)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = config['web']['baseUrl']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        #wd.get("http://localhost:8080/addressbook")
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()