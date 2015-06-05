__author__ = 'lemontree'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_homepage(self, wd):
        wd = self.wd
        if not(wd.current_url.endswith("/addressbook/")):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()