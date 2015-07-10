__author__ = 'lemontree'
from model.contact import Contacts
from model.group import Group
import random

def test_delete_contact_to_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contacts(name="FirstName",lastname="FirstLastName", nickname="Nickname"))
    if app.group.count() == 0:
        app.group.create(Group(name="first_group"))
    old_contacts_in_group = orm.get_contacts_in_group(Group(id="144"))
    delete_contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group(delete_contact.id)
    new_contacts_in_group = orm.get_contacts_in_group(Group(id="144"))
    old_contacts_in_group.remove(delete_contact)
    assert sorted(old_contacts_in_group, key = Contacts.id_or_max) == sorted(new_contacts_in_group, key = Contacts.id_or_max)