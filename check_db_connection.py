__author__ = 'lemontree'

from fixture.orm import ORMFixture
from model.group import Group
import random

db = ORMFixture(host = "127.0.0.1", name = "addressbook", user = "root", password = "")

try:
    l = db.get_contacts_not_in_group(Group(id="144"))
    print (random.choice(db.get_contact_list()))
    print("end of random")
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
