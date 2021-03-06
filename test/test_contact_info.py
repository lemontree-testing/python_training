__author__ = 'lemontree'
import re
from model.contact import Contacts

def test_information_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)
    assert contact_from_homepage.address == contact_from_editpage.address
    assert contact_from_homepage.firstname == contact_from_editpage.firstname
    assert contact_from_homepage.lastname == contact_from_editpage.lastname
    assert contact_from_homepage.all_email_from_homepage == merge_email_like_on_homepage(contact_from_editpage)

def test_information_on_homepage_vs_db(app, db):
    contact_from_homepage = app.contact.get_contact_list()
    def clean(contact):
        return Contacts(id=contact.id, name=contact.firstname.strip(), lastname=contact.lastname.strip(), address=contact.address.strip(),
                        all_email_from_homepage=merge_email_like_on_homepage(contact), all_phones_from_homepage=merge_phones_like_on_homepage(contact))
    contact_from_db = map(clean, db.get_contact_list())
    assert sorted(contact_from_homepage, key=Contacts.id_or_max) == sorted(contact_from_db, key=Contacts.id_or_max)


def clear(s):
    return re.sub("[() -]","", s)

def test_phones_on_viewpage(app):
    contact_from_viewpage = app.contact.get_contact_info_from_viewpage(0)
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_viewpage.homephone == contact_from_editpage.homephone
    assert contact_from_viewpage.workphone == contact_from_editpage.workphone
    assert contact_from_viewpage.mobilephone == contact_from_editpage.mobilephone
    assert contact_from_viewpage.secondaryphone == contact_from_editpage.secondaryphone

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email_2, contact.email_3])))