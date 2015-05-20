# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contacts

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password,):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def add_new_contact(self, wd, contact):
        #init_new_contact_creation
        wd.find_element_by_link_text("add new").click()
        #fill new contact information
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        if not wd.find_element_by_xpath(contact.day_of_birth).is_selected():
            wd.find_element_by_xpath(contact.day_of_birth).click()
        wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath(contact.month_of_birth).is_selected():
            wd.find_element_by_xpath(contact.month_of_birth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year_of_birth)
        #submit new contact
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd,  username="admin", password="secret")
        self.add_new_contact(wd, Contacts(name="Name",lastname="LastName", nickname="Nickname", company="AppliedTests",email="name.lastname@applied-testing.ru",day_of_birth="//div[@id='content']/form/select[1]//option[3]",month_of_birth="//div[@id='content']/form/select[2]//option[2]",year_of_birth="1980"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd,  username="admin", password="secret")
        self.add_new_contact(wd, Contacts(name="",lastname="", nickname="", company="",email="",day_of_birth="//div[@id='content']/form/select[1]//option[2]",month_of_birth="//div[@id='content']/form/select[2]//option[1]",year_of_birth=""))
        self.return_to_homepage(wd)
        self.logout(wd)

    def test_add_nolastname_contact(self):
        #in this test email information provides the Last Name of the contact
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd,  username="admin", password="secret")
        self.add_new_contact(wd, Contacts(name="NameNoLastName",lastname="", nickname="Nickname", company="AppliedTests",email="Mystic.Creature@applied-testing.ru",day_of_birth="//div[@id='content']/form/select[2]//option[3]",month_of_birth="//div[@id='content']/form/select[2]//option[2]",year_of_birth="000000"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def test_add_emailinfo_contact(self):
        #in this test email information provides the First Name and the Last Name of the contact.
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd,  username="admin", password="secret")
        self.add_new_contact(wd, Contacts(name="",lastname="", nickname="Nickname", company="",email="Mystic.CreatureBro@applied-testing.ru",day_of_birth="//div[@id='content']/form/select[2]//option[3]",month_of_birth="//div[@id='content']/form/select[2]//option[2]",year_of_birth="000000"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
