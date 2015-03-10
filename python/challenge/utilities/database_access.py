from models.Person import Person
import sqlite3


class DatabaseManager:
    def __init__(self):
        self.add_person_query = ("INSERT INTO people "
                                 "(id, name, age, phone, birthday) "
                                 "VALUES (?, ?, ?, ?, ?)")
        self.create_table_people = "CREATE TABLE people(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, phone TEXT," \
                                   " birthday DATE)"
        self.retrive_all = "SELECT * FROM people"
        self.update_phone = "UPDATE people SET phone = ? WHERE id = ?"

    def start_connection(self, config):
        cnx = sqlite3.connect(config)
        setattr(self, "cnx", cnx)

    def stop_connection(self):
        getattr(self, "cnx").close()

    def create_table(self):
        try:
            cursor = getattr(self, "cnx")
            cursor.execute(self.create_table_people)
            getattr(self, "cnx").commit()
        except sqlite3.OperationalError as e:
            if e.message.__contains__('already exists'):
                print "The table already exists"

    def add_person(self, person):
        try:
            cursor = getattr(self, "cnx").cursor()
            person_data = person.serialize()
            cursor.execute(self.add_person_query, person_data)
            getattr(self, "cnx").commit()
        except sqlite3.IntegrityError:
            print "This record already exists in the database {0} - {1}".format(getattr(person, "id"),
                                                                                getattr(person, "name"))

    def get_people(self):
        people = getattr(self, "cnx").cursor()
        people.execute(self.retrive_all)
        people_list = list()
        for data in people:
            person = Person(data[0], data[1], data[2], data[3], data[4])
            people_list.append(person)
        return people_list