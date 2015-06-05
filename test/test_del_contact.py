__author__ = 'lemontree'

from model.contact import Contacts

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(name="FirstName",lastname="FirstLastName", nickname="Nickname"))
    app.contact.delete_first_contact()
