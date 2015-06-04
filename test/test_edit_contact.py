__author__ = 'lemontree'

from model.contact import Contacts

def test_edit_contact(app):
    app.contact.edit_first_contact(Contacts(name="New_Name",lastname="New_LastName", nickname="New_Nickname", company="New_AppliedTests",email="new.name.lastname@applied-testing.ru",year_of_birth="1990"))

def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contacts(lastname="YetAnotherLastName"))
