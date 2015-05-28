# -*- coding: utf-8 -*-
from model.contact import Contacts

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contacts(name="Name",lastname="LastName", nickname="Nickname", company="AppliedTests",email="name.lastname@applied-testing.ru",year_of_birth="1980"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contacts(name="",lastname="", nickname="", company="",email="",year_of_birth=""))
    app.session.logout()

