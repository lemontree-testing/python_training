__author__ = 'lemontree'

from model.contact import Contacts
import random
#from random import randrange

def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contacts(name="FirstName",lastname="FirstLastName", nickname="Nickname"))
    old_contacts = db.get_contact_list()
    edit_contact = random.choice(old_contacts)
    contact=Contacts(name="New_Name",lastname="New_LastName", nickname="New_Nickname", company="New_AppliedTests",email="new.name.lastname@applied-testing.ru",year_of_birth="1990")
    contact.id = edit_contact.id
    app.contact.edit_contact_by_id(contact.id,contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(edit_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contacts.id_or_max) == sorted(new_contacts, key = Contacts.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)



