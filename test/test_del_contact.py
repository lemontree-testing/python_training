__author__ = 'lemontree'
from model.contact import Contacts

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()