from models.Person import Person
import sqlite3


class DatabaseManager:
    def __init__(self, database):
        self.database = database
        self.add_person_query = ("INSERT INTO people "
                                 "(id, name, age, phone, birthday) "
                                 "VALUES (?, ?, ?, ?, ?)")
        self.create_table_people = "CREATE TABLE people(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, phone TEXT," \
                                   " birthday DATE)"
        self.retrieve_all = "SELECT * FROM people"
        self.update_phone_query = "UPDATE people SET phone = ? WHERE id = ?"
        self.update_name_query = "UPDATE people SET name = ? WHERE id = ?"
        self.find_person_query = "SELECT * FROM people WHERE id = ?"

    def start_connection(self, config):
        cnx = sqlite3.connect(config)
        setattr(self, "cnx", cnx)

    def stop_connection(self):
        getattr(self, "cnx").close()

    def create_table(self):
        try:
            self.start_connection(self.database)
            cursor = getattr(self, "cnx")
            cursor.execute(self.create_table_people)
            getattr(self, "cnx").commit()
            self.stop_connection()
        except sqlite3.OperationalError as e:
            if e.message.__contains__('already exists'):
                print "The table already exists"

    def add_person(self, person):
        try:
            self.start_connection(self.database)
            cursor = getattr(self, "cnx").cursor()
            person_data = person.serialize()
            cursor.execute(self.add_person_query, person_data)
            getattr(self, "cnx").commit()
            self.stop_connection()
        except sqlite3.IntegrityError:
            print "This record already exists in the database {0} - {1}".format(getattr(person, "id"),
                                                                                getattr(person, "name"))

    def get_people(self):
        self.start_connection(self.database)
        people = getattr(self, "cnx").cursor()
        people.execute(self.retrieve_all)
        people_list = list()
        self.stop_connection()
        for data in people:
            person = Person(data[0], data[1], data[2], data[3], data[4])
            people_list.append(person)
        return people_list

    def find_person(self, person_id):
        self.start_connection(self.database)
        cursor = getattr(self, "cnx").cursor()
        cursor.execute(self.find_person_query, str(person_id))
        self.stop_connection()
        return cursor.fetchall()

    def populate_table(self, people):
        self.start_connection(self.database)
        for person in people:
            cursor = getattr(self, "cnx").cursor()
            cursor.execute(self.add_person_query, person.serialize())
            getattr(self, "cnx").commit()
        self.stop_connection()

    def update_phone(self, person_id, phone):
        self.start_connection(self.database)
        cursor = getattr(self, "cnx").cursor()
        cursor.execute(self.update_phone_query, (str(phone), str(person_id)))
        self.stop_connection()

    def update_name(self, person_id, name):
        self.start_connection(self.database)
        cursor = getattr(self, "cnx").cursor()
        cursor.execute(self.update_name_query, (str(name), str(person_id)))
        self.stop_connection()