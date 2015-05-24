# -*- coding: utf-8 -*-
import pytest
from contact import Contacts
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contacts(name="Name",lastname="LastName", nickname="Nickname", company="AppliedTests",email="name.lastname@applied-testing.ru",year_of_birth="1980"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contacts(name="",lastname="", nickname="", company="",email="",year_of_birth=""))
    app.logout()
