from utilities.file_operations import FileManager
from utilities.file_operations import get_config
from utilities.database_access import DatabaseManager


class App:

    def __init__(self):
        self.config = get_config()
        self.file_manager = FileManager()
        self.db_manager = DatabaseManager(self.config["database_conn_info"])
        self.options = {"generate_report": 1, "update_person": 2, "exit": 3}
        self.update_options = {"updtae_name": 1, "update_phone": 2, "cancel": 3}

    def display_menu(self):
        print("*********************************************\n"
              "**                                         **\n"
              "**                AGENDA                   **\n"
              "*********************************************\n"
              "**                                         **\n"
              "**      1. GENERATE REPORT(XML)            **\n"
              "**      2. UPDATE PERSON DETAILS           **\n"
              "**      3. EXIT                            **\n"
              "*********************************************")

    def display_update_menu(self):
        print("*********************************************\n"
              "**                                         **\n"
              "**                AGENDA                   **\n"
              "*********************************************\n"
              "**                                         **\n"
              "**      1. UPDATE NAME                     **\n"
              "**      2. UPDATE PHONE NUMBER             **\n"
              "**      3. CANCEL                          **\n"
              "**                                         **\n"
              "*********************************************")

    def main(self):
        user_option = 0
        while user_option < 3:
            self.display_menu()
            try:
                user_option = int(raw_input('>Option: '))
                if user_option > 3 or user_option < 0:
                    raise ValueError
                if user_option == self.options["generate_report"]:
                    self.generate_xml_report()
                elif user_option == self.options["update_person"]:
                    user_id = int(raw_input('>Enter the id you want to modify: '))
                    self.update_person_details(user_id)

            except ValueError:
                print('Not a valid option')
                user_option = 0
        print('Bye...')

    def start(self):
        """Initializes the table PEOPLE reading the input file"""
        people = self.file_manager.parse_init_people_file()
        self.db_manager.create_table()
        self.db_manager.populate_table(people)

    def generate_xml_report(self):
        people = self.db_manager.get_people()
        self.file_manager.generate_report(people)

    def update_person_details(self, user_id):
        print '\n'*2
        option = 0
        count = self.db_manager.find_person(user_id)
        print("Current Person information {}", count)
        if count.__len__() == 0:
            print('The id does not exist. Please choose other.')
            return

        while option < 3:
            self.display_update_menu()
            try:
                option = int(raw_input('>Option: '))
                if option > 3 or option < 0:
                    raise ValueError
                if option == self.update_options["updtae_name"]:
                    new_name = raw_input("Enter new name: ")
                    self.update_name(user_id, new_name)
                if option == self.update_options["update_phone"]:
                    new_phone = raw_input("Enter new phone number: ")
                    self.update_phone(user_id, new_phone)
            except ValueError:
                print('Not a valid option')
                option = 0
        print 'update section'

    def update_name(self, person_id, new_name):
        self.db_manager.update_name(person_id, new_name)

    def update_phone(self, person_id, new_phone):
        self.db_manager.update_phone(person_id, new_phone)

if __name__ == '__main__':
    app = App()
    app.start()
    app.main()