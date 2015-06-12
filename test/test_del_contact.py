__author__ = 'lemontree'

from model.contact import Contacts
from random import randrange
def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(name="FirstName",lastname="FirstLastName", nickname="Nickname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1]= []
    assert len(old_contacts) == len(new_contacts)
