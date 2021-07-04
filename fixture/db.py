import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = list()
        with self.connection.cursor() as cursor:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id, name, header, footer = row
                group_list.append(Group(name=name, header=header, footer=footer, id=str(id)))
        return group_list

    def get_contact_list(self):
        contact_list = list()
        with self.connection.cursor() as cursor:
            cursor.execute('''
                              SELECT id, firstname, lastname, address,
                                     home, mobile, work, phone2,
                                     email, email2, email3
                              FROM addressbook
                              WHERE deprecated="0000-00-00 00:00:00"
                          ''')
            for row in cursor:
                (
                    cid, firstname, lastname, address,
                    home, mobile, work, phone2,
                    email, email2, email3
                ) = row
                contact_list.append(Contact(
                    cid=str(cid), firstname=firstname, lastname=lastname, address=address,
                    home_phone=home, mobile_phone=mobile, work_phone=work, secondary_phone=phone2,
                    email=email, email2=email2, email3=email3
                ))
        return contact_list

    def destroy(self):
        self.connection.close()