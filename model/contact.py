__author__ = 'lemontree'

from sys import maxsize

class Contacts:
    def __init__(self,name=None,lastname=None,nickname=None,company=None,email=None,year_of_birth=None,id= None):
        self.firstname=name
        self.lastname=lastname
        self.nickname=nickname
        self.company=company
        self.email=email
        self.year_of_birth=year_of_birth
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname) and (self.lastname==other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize