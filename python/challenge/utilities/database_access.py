import mysql.connector as mc


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
        cursor = getattr(self, "cnx").cursor()
        person_data = person.serialize()
        cursor.execute(DatabaseManager.add_person_query, person_data)
        getattr(self, "cnx").commit()