__author__ = 'lemontree'

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def enter_contact_information(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("email", contact.email)
        self.change_field_value("byear", contact.year_of_birth)

    def create(self, contact):
        wd = self.app.wd
        self.app.open_homepage(wd)
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
        self.app.open_homepage(wd)
        #select contact for deletion
        wd.find_element_by_name("selected[]").click()
        #submit contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_homepage()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_homepage(wd)
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

