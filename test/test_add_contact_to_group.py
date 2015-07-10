__author__ = 'lemontree'

from model.contact import Contacts
from model.group import Group
import random

def test_add_contact_to_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contacts(name="FirstName",lastname="FirstLastName", nickname="Nickname"))
    if app.group.count() == 0:
        app.group.create(Group(name="first_group"))
    old_contacts_in_group = orm.get_contacts_in_group(Group(id="144"))
    edit_contact = random.choice(orm.get_contacts_not_in_group(Group(id="144")))
    app.contact.change_group_for_contact(edit_contact.id)
    new_contacts_in_group = orm.get_contacts_in_group(Group(id="144"))
    old_contacts_in_group.append(edit_contact)
    assert sorted(old_contacts_in_group, key = Contacts.id_or_max) == sorted(new_contacts_in_group, key = Contacts.id_or_max)
