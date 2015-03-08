from models.Person import Person
import xml.dom.minidom as md


class FileManager:
    def parse_init_people_file(self):
        """Reads input file and parse each line to a Person object which is inserted in People list"""
        people = dict()
        input_file = open("input.csv", "r", 1)
        data = input_file.read().splitlines()

        for ln in data:
            data = ln.split(',')
            person = Person()
            setattr(person, "id", data[0])
            setattr(person, "name", data[1])
            setattr(person, "age", data[2])
            setattr(person, "phone_number", data[3])
            setattr(person, "birthday", data[4])
            people[getattr(person, "id")] = person
        input_file.close()
        return people

    def generate_report(self, people):
        """Create the xml structure"""
        agenda = md.parseString('<agenda>  </agenda>')
        for index in people:
            person = people[index]
            person_el = self.create_person_node(agenda, person)
            agenda.documentElement.appendChild(person_el)
        self.write_file_report(agenda, "agenda.xml")

    def create_person_node(self, parent, data):
        person_el = parent.createElement('person')
        id = parent.createElement('id')
        name = parent.createElement('name')
        age = parent.createElement('age')
        phone = parent.createElement('phone_number')
        birthday = parent.createElement('birthday')
        id.appendChild(parent.createTextNode(getattr(data, 'id')))
        name.appendChild(parent.createTextNode(getattr(data, 'name')))
        age.appendChild(parent.createTextNode(getattr(data, 'age')))
        phone.appendChild(parent.createTextNode(getattr(data, 'phone_number')))
        birthday.appendChild(parent.createTextNode(getattr(data, 'birthday')))
        person_el.appendChild(id)
        person_el.appendChild(name)
        person_el.appendChild(age)
        person_el.appendChild(phone)
        person_el.appendChild(birthday)
        return person_el

    def write_file_report(self, agenda, file_path):
        """Writes the xml file in the specified file"""
        report = open(file_path, mode="w", buffering=1)
        report.write(agenda.toprettyxml(encoding="utf-8"))
        report.close()


def get_config():
    """Reads and parse configurations from the config file"""
    config_file = open("config_files/config.properties", "r")
    configurations = config_file.read().splitlines()
    config = dict()
    for ln in configurations:
        key_pairs = ln.split("=")
        if key_pairs[0] != "database_conn_info":
            config[key_pairs[0]] = key_pairs[1]
        else:
            config[key_pairs[0]] = serialize_db_config(key_pairs[1])
    return config


def serialize_db_config(config):
    db_config = dict()
    config = config.split(",")
    for values in config:
        key_value = values.split(":")
        db_config[key_value[0]] = key_value[1]
    return db_config