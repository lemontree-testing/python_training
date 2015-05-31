__author__ = 'lemontree'

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def enter_contact_information(self, contact):
        wd = self.app.wd
        #fill in new contact information
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
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year_of_birth)

    def create(self, contact):
        wd = self.app.wd
        #init_new_contact_creation
        wd.find_element_by_link_text("add new").click()
        #fill in new contact information
        self.enter_contact_information(contact)
        #submit new contact
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        #select contact for deletion
        wd.find_element_by_name("selected[]").click()
        #submit contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_homepage()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        #select first contact_to edit
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        #fill in new contact information
        self.enter_contact_information(contact)
        #submit edited contact
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

