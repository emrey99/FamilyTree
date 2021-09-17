class OutputMessages:
    def __init__(self):
        pass

    def invalid_input(self):
        print("Please import valid input")

    def type_help_message(self):
        print("Please type 'help' on the console so you can see all the commands")

    def select_any_command_message(self):
        print("Select one of the commands so you can see the information needed so you can execute the command")

    def child_insert_message(self):
        print("Please type the name you want to insert and the city where the person is born")

    def child_added_message(self):
        print("Child successfully added")

    def child_remove_message(self):
        print("Please type the child name you want to remove")

    def child_removed_successfully_message(self):
         print("Child successfully removed")

    def insert_father_requirements_message(self):
        print("Please type the name and the city you want to insert, also the person_id which corresponds to the child's ID")

    def father_added_message(self):
        print("Father successfully added")

    def father_remove_requirements(self):
        print("Please type the father name you want to remove")

    def father_removed_message(self):
        print("Father successfully removed")

    def insert_mother_requirements_message(self):
        print("Please type the name and the city you want to insert, also the person_id which corresponds to the child's ID")

    def mother_added_message(self):
        print("Mother successfully added")

    def mother_remove_requirements(self):
        print("Please type the mother name you want to remove")

    def mother_removed_message(self):
        print("Mother successfully removed")