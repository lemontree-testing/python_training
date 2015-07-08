__author__ = 'lemontree'
import mysql.connector
from model.group import Group
from model.contact import Contacts

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, nickname, company, address, home, work, mobile, fax, email, email2, email3, byear from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, nickname, company, address, home, work, mobile, fax, email, email2, email3, byear) = row
                list.append(Contacts(id=str(id), name=firstname, lastname=lastname, nickname=nickname, company=company,
                                     address=address, homephone=home, mobilephone=mobile,secondaryphone=fax, email=email, email_2=email2, email_3=email3, year_of_birth=byear))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
