from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, email=None, email2=None, email3=None, home_phone=None, mobile_phone=None,
                 work_phone=None, secondary_phone=None, all_phones_from_home_page=None, all_emails_from_home_page=None, cid=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = cid

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def __lt__(self, other):
        return self.id < other.id

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize
