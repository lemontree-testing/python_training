__author__ = 'lemontree'

from model.contact import Contacts
import re

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
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("fax", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
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
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage(wd)
        #select contact for deletion
        wd.find_elements_by_name("selected[]")[index].click()
        #submit contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_homepage(wd)
        #select contact for deletion
        wd.find_element_by_css_selector("input[id='%s']" % id).click()
        #submit contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def open_contact_editpage_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage(wd)
        #select a contact_to edit
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        #fill in new contact information

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_editpage_by_index(index)
        self.enter_contact_information(contact)
        #submit edited contact
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def open_contact_editpage_by_id(self, id):
        wd = self.app.wd
        self.app.open_homepage(wd)
        #select a contact_to edit
        wd.find_element_by_xpath("//a[contains(@href,'edit.php?id=%s')]" % id).click()
        #fill in new contact information

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_editpage_by_id(id)
        self.enter_contact_information(contact)
        #submit edited contact
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def change_group_for_contact(self, contact_id):
        wd = self.app.wd
        self.app.open_homepage(wd)
        wd.find_element_by_id("%s" % contact_id).click()
        wd.find_element_by_xpath("//div[@class='right']/select//option[16]").click()
        wd.find_element_by_name("add").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_contact_from_group(self, contact_id):
        wd = self.app.wd
        self.app.open_homepage(wd)
        wd.get("http://localhost/addressbook/?group=new_name")
        wd.find_element_by_id("%s" % contact_id).click()
        wd.find_element_by_name("remove").click()
        self.return_to_homepage()
        self.contact_cache = None

    def view_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage(wd)
        #select a contact_to view
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()
        self.contact_cache = None

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_homepage(wd)
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_homepage(wd)
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_xpath(".//td[3]").text
                lastname = element.find_element_by_xpath(".//td[2]").text
                address = element.find_element_by_xpath(".//td[4]").text
                all_email = element.find_element_by_xpath(".//td[5]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contacts(name = firstname, lastname = lastname, id = id, address = address,
                                                   all_phones_from_homepage = all_phones, all_email_from_homepage = all_email))
        return list(self.contact_cache)


    def get_contact_info_from_editpage(self, index):
        wd = self.app.wd
        self.open_contact_editpage_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contacts(name = firstname, lastname = lastname, address = address,
                       homephone = homephone, workphone = workphone, mobilephone = mobilephone,
                       email = email, email_2 = email_2, email_3 = email_3, id = id)

    def get_contact_info_from_viewpage(self, index):
        wd = self.app.wd
        self.view_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone =  re.search("W: (.*)", text).group(1)
        mobilephone =  re.search("M: (.*)", text).group(1)
        return Contacts(homephone = homephone, workphone = workphone, mobilephone = mobilephone)