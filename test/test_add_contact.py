# -*- coding: utf-8 -*-
from model.contact import Contacts

def test_add_contact(app):
    app.contact.create(Contacts(name="Name",lastname="LastName", nickname="Nickname", company="AppliedTests",email="name.lastname@applied-testing.ru",year_of_birth="1980"))

def test_add_empty_contact(app):
    app.contact.create(Contacts(name="",lastname="", nickname="", company="",email="",year_of_birth=""))

