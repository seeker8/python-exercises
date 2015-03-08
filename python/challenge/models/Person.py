class Person:

    def __init__(self, id=0, name="", age="", phone_number="", birthday=""):
        self.id = id
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.birthday = birthday

    def __str__(self):
        person_str = 'ID: ' + str(self.id) + '\n'
        person_str += 'Name: ' + str(self.name) + '\n'
        person_str += 'Age: ' + str(self.age) + '\n'
        person_str += 'Phone: ' + str(self.phone_number) + '\n'
        person_str += 'Birthday: ' + str(self.birthday) + '\n'
        return person_str

    def serialize(self):
        return self.id, self.name, self.age, self.phone_number, self.birthday