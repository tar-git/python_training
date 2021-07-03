from fixture.common import random_string
from model.group import Group
import re
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def clear_group_name(name):
    cleared_name = re.sub(r' {2,}', ' ', name)
    return cleared_name.strip()


test_data = [Group(name="", header="", footer="")] + [Group(
    clear_group_name(random_string("name_", 10)),
    random_string("header_", 10),
    random_string("footer_", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))