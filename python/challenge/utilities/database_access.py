import mysql.connector as mc


class DatabaseManager:
    queries = dict()
    queries['insert'] = ("INSERT INTO people "
                         "(id, name_, age, phone, birthday) "
                         "VALUES (%s, %s, %s, %s, %s)")

    def start_connection(self, config):
        cnx = mc.connect(**config)
        setattr(self, "cnx", cnx)

    def stop_connection(self):
        getattr(self, "cnx").close()

    def insert_person(self, person):
        cursor = getattr(self, "cnx").cursor()
        person_data = person.serialize()
        cursor.execute(DatabaseManager.queries['insert'], person_data)
        getattr(self, "cnx").commit()