# -*- coding: utf-8 -*-
from model.contact import Contacts

def test_add_contact(app):
    contact=Contacts(name="Name",lastname="LastName", nickname="Nickname", company="AppliedTests",email="name.lastname@applied-testing.ru",year_of_birth="1980")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contacts.id_or_max) == sorted(new_contacts, key = Contacts.id_or_max)

def test_add_empty_contact(app):
    contact=Contacts(name="",lastname="", nickname="", company="",email="",year_of_birth="")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contacts.id_or_max) == sorted(new_contacts, key = Contacts.id_or_max)

