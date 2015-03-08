import mysql.connector as mc
from mysql.connector import errors

class DatabaseManager:
    add_person_query = ("INSERT INTO people "
                        "(id, name_, age, phone, birthday) "
                        "VALUES (%s, %s, %s, %s, %s)")

    def start_connection(self, config):
        cnx = mc.connect(**config)
        setattr(self, "cnx", cnx)

    def stop_connection(self):
        getattr(self, "cnx").close()

    def add_person(self, person):
        try:
            cursor = getattr(self, "cnx").cursor()
            person_data = person.serialize()
            cursor.execute(DatabaseManager.add_person_query, person_data)
            getattr(self, "cnx").commit()
        except errors.IntegrityError:
            print "This record already exists in the database {0} - {1}".format(getattr(person, "id"),
                                                                                getattr(person, "name"))