# -*- coding: utf-8 -*-
from model.contact import Contacts

def test_add_contact(app):
    contact=Contacts(name = "Name",lastname = "LastName", nickname = "Nickname", company = "AppliedTests",
                     address = "New Address, New City, 666/42@3432r", homephone = "home9999999999", workphone = "work00000000",
                     mobilephone = "mobile32141353", secondaryphone = "5446446", email = "name.lastname@applied-testing.ru",
                     email_2 = "email2@newmegamail.ru", email_3 = "happymail@travel.ru", year_of_birth = "1980")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contacts.id_or_max) == sorted(new_contacts, key = Contacts.id_or_max)

#def test_add_empty_contact(app):
#    contact=Contacts(name="",lastname="", nickname="", company="",email="",year_of_birth="")
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key = Contacts.id_or_max) == sorted(new_contacts, key = Contacts.id_or_max)

