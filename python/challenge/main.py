from utilities.file_operations import FileManager
from utilities.file_operations import get_config
from utilities.database_access import DatabaseManager

class App:

    def __init__(self):
        self.config = get_config()
        self.file_manager = FileManager()
        self.db_manager = DatabaseManager()

    def display_menu(self):
        print("*********************************************\n"
              "**                                         **\n"
              "**                AGENDA                   **\n"
              "*********************************************\n"
              "**                                         **\n"
              "**      1. GENERATE REPORT(XML)            **\n"
              "**      5. EXIT                            **\n"
              "*********************************************")

    def main(self):
        self.start()
        user_option = 0
        while user_option != 5:
            self.display_menu()
            try:
                user_option = int(raw_input('>Option: '))
            except ValueError:
                print('Not a valid option')
                user_option = 0
        print('Bye...')

    def start(self):
        """Initializes the table PEOPLE reading the input file"""
        people = self.file_manager.parse_init_people_file()
        self.db_manager.start_connection(self.config["database_conn_info"])
        for index in people:
            self.db_manager.add_person(people[index])
        self.db_manager.stop_connection()

if __name__ == '__main__':
    app = App()
    app.main()