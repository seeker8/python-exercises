from utilities.file_operations import FileManager
from utilities.database_access import DatabaseManager
from models.Person import Person

class App:
    def display_menu(self):
        print("*********************************************\n"
              "**                                         **\n"
              "**                AGENDA                   **\n"
              "*********************************************\n"
              "**                                         **\n"
              "**      1. START                           **\n"
              "**      5. EXIT                            **\n"
              "*********************************************")

    def main(self):
        user_option = 1
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
        fileManager = FileManager()
        people = fileManager.parse_file()

if __name__ == '__main__':
    app = App()
    app.main()