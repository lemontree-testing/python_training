__author__ = 'lemontree'

from model.contact import Contacts

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(name="FirstName",lastname="FirstLastName", nickname="Nickname"))
    old_contacts = app.contact.get_contact_list()
    contact=Contacts(name="New_Name",lastname="New_LastName", nickname="New_Nickname", company="New_AppliedTests",email="new.name.lastname@applied-testing.ru",year_of_birth="1990")
    app.contact.edit_first_contact(contact)
    contact.id = old_contacts[0].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0]=contact
    assert sorted(old_contacts, key = Contacts.id_or_max) == sorted(new_contacts, key = Contacts.id_or_max)

#def test_edit_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contacts(name="FirstName",lastname="FirstLastName", nickname="Nickname"))
#    app.contact.edit_first_contact(Contacts(lastname="YetAnotherLastName"))
