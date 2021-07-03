from fixture.common import random_string
from model.contact import Contact
import re
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

test_data = [ Contact(
        firstname= "", lastname= "",
        address= "", email= "", email2= "",
        email3= "", home_phone= "", mobile_phone= "",
        work_phone= "", secondary_phone= ""
)] + [
    Contact(
        firstname=random_string("firstname_", 10),
        lastname=random_string("lastname_", 10),
        address=random_string("address_", 10),
        email=random_string("email_", 10),
        email2=random_string("email2_", 10),
        email3=random_string("email3_", 10),
        home_phone=random_string("home_phone_", 10),
        mobile_phone=random_string("mobile_phone_", 10),
        work_phone=random_string("work_phone_", 10),
        secondary_phone=random_string("secondary_phone_", 10)
    )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))