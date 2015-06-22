# -*- coding: utf-8 -*-
from model.contact import Contacts
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix + "".join(random.choice(symbols)for i in range(random.randrange(maxlen)))

testdata = [Contacts(name = "",lastname = "", nickname = "", company = "", address = "", homephone = "", email = "",year_of_birth = "")] + [
           Contacts(name = random_string("Name", 20), lastname = random_string("LastName", 30), nickname = random_string("Nickname", 40),
                     company = random_string("Company", 30), address = random_string("Addr", 100), homephone = random_string("home", 10),
                     email = random_string("mail1",20), year_of_birth = random.randrange(0000,1000)) for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contacts.id_or_max) == sorted(new_contacts, key = Contacts.id_or_max)



