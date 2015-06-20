__author__ = 'lemontree'

from sys import maxsize

class Contacts:
    def __init__(self, name = None, lastname = None, nickname = None, address = None, company = None, homephone = None,
                 workphone = None, mobilephone = None, secondaryphone = None, email = None, email_2 = None, email_3 = None,
                 year_of_birth = None, all_phones_from_homepage = None,
                 all_email_from_homepage = None, id = None):
        self.firstname = name
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.company = company
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.year_of_birth = year_of_birth
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_email_from_homepage = all_email_from_homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname) and (self.lastname==other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize