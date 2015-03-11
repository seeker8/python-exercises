from utilities.file_operations import FileManager
from utilities.file_operations import get_config
from utilities.database_access import DatabaseManager


class App:

    def __init__(self):
        self.config = get_config()
        self.file_manager = FileManager()
        self.db_manager = DatabaseManager()
        self.options = {"generate_report": 1, "update_person": 2, "exit": 5}

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
        while user_option < 5:
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
        self.db_manager.start_connection(self.config["database_conn_info"])
        self.db_manager.create_table()
        for person in people:
            self.db_manager.add_person(person)
        self.db_manager.stop_connection()

    def generate_xml_report(self):
        self.db_manager.start_connection(self.config["database_conn_info"])
        people = self.db_manager.get_people()
        self.db_manager.stop_connection()
        self.file_manager.generate_report(people)

    def update_person_details(self, user_id):
        print '\n'*2
        option = 0
        self.db_manager.start_connection(self.config["database_conn_info"])
        count = self.db_manager.find_person(user_id)
        self.db_manager.stop_connection()
        if count.__len__() == 0:
            print('The id does not exist. Please choose other.')
            return

        while option < 3:
            self.display_update_menu()
            try:
                option = int(raw_input('>Option: '))
                if option > 3 or option < 0:
                    raise ValueError
            except ValueError:
                print('Not a valid option')
                option = 0
        print 'update section'

if __name__ == '__main__':
    app = App()
    app.start()
    app.main()