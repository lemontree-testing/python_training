__author__ = 'lemontree'
from model.contact import Contacts
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix + "".join(random.choice(symbols)for i in range(random.randrange(maxlen)))

testdata = [Contacts(name = "",lastname = "", nickname = "", company = "", address = "", homephone = "", email = "",year_of_birth = "")] + [
           Contacts(name = random_string("Name", 20), lastname = random_string("LastName", 30), nickname = random_string("Nickname", 40),
                     company = random_string("Company", 30), address = random_string("Addr", 100), homephone = random_string("home", 10),
                     email = random_string("mail1",20), year_of_birth = random.randrange(0000,1000)) for i in range(5)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))