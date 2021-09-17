from common.enums import CommandType
from core.Controller import Controller
from common.constants.OutputMessages import OutputMessages

outPutMessages = OutputMessages()
controller = Controller()


class Engine:
    def __init__(self):
        pass


    def run(self):

        while True:

            command = input()

            if command != "help":

                 outPutMessages.type_help_message()

            elif command == "help":

                commands = CommandType.commands

                for i in commands:

                    print(i)

                outPutMessages.select_any_command_message()

                command = input()

                if command in commands:

                    if command == "insert_child":

                        outPutMessages.child_insert_message()

                        inputInsertChild = input().split()

                        name_of_child = inputInsertChild[0]

                        place_of_birth = inputInsertChild[1]

                        if type(name_of_child) == str and type(place_of_birth) == str:

                            controller.insert_child(name_of_child,place_of_birth)

                            outPutMessages.child_added_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "remove_child":

                        outPutMessages.child_remove_message()

                        inputRemoveChild = input().split()

                        name_of_child = inputRemoveChild[0]

                        if type(name_of_child)==str:

                            controller.remove_child(name_of_child)

                            outPutMessages.child_remove_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "insert_father":

                        outPutMessages.insert_father_requirements_message()

                        inputInsertFather = input().split()

                        name_of_father = inputInsertFather[0]

                        place_of_birth = inputInsertFather[1]

                        Id_of_father = int(inputInsertFather[2])

                        if type(name_of_father) == str and type(place_of_birth) == str and type(Id_of_father) == int:

                            controller.insert_father(name_of_father, place_of_birth,Id_of_father)

                            outPutMessages.father_added_message()

                        else:
                            outPutMessages.invalid_input()

                    elif command == "remove_father":

                        outPutMessages.father_remove_requirements()

                        inputRemoveFather = input().split()

                        name_of_father = inputRemoveChild[0]

                        if type(name_of_child) == str:

                            controller.remove_father(name_of_father)

                            outPutMessages.father_removed_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "insert_mother":

                        outPutMessages.insert_mother_requirements_message()

                        inputInsertMother = input().split()

                        name_of_mother = inputInsertMother[0]

                        place_of_birth = inputInsertMother[1]

                        Id_of_mother = int(inputInsertMother[2])

                        if type(name_of_mother) == str and type(place_of_birth) == str and type(Id_of_mother) == int:

                            controller.insert_mother(name_of_mother, place_of_birth, Id_of_mother)

                            outPutMessages.mother_added_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "remove_mother":

                        outPutMessages.mother_remove_requirements()

                        inputRemoveMother = input().split()

                        name_of_mother = inputRemoveChild[0]

                        if type(name_of_mother) == str:

                            controller.remove_mother(name_of_mother)

                            outPutMessages.mother_removed_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "insert_grand_father1":

                        outPutMessages.insert_father_requirements_message()

                        input_insert_grand_father1 = input().split()

                        name_of_grand_father1 = input_insert_grand_father1[0]

                        place_of_birth = input_insert_grand_father1[1]

                        Id_of_grand_father1 = int(input_insert_grand_father1[2])

                        if type(name_of_grand_father1) == str and type(place_of_birth) == str and type(Id_of_grand_father1) == int:

                            controller.insert_grand_father1(name_of_grand_father1, place_of_birth, Id_of_grand_father1)

                            outPutMessages.father_added_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "insert_grand_father2":

                        outPutMessages.insert_father_requirements_message()

                        input_insert_grand_father2 = input().split()

                        name_of_grand_father2 = input_insert_grand_father2[0]

                        place_of_birth = input_insert_grand_father2[1]

                        Id_of_grand_father2 = int(input_insert_grand_father2[2])

                        if type(name_of_grand_father2) == str and type(place_of_birth) == str and type(
                                Id_of_grand_father2) == int:

                            controller.insert_grand_father2(name_of_grand_father2, place_of_birth, Id_of_grand_father2)

                            outPutMessages.father_added_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "remove_grand_father1":

                        outPutMessages.father_remove_requirements()

                        input_remove_grand_father1 = input().split()

                        name_of_grand_father1 = input_remove_grand_father1[0]

                        if type(name_of_mother) == str:

                            controller.remove_grand_father1(name_of_grand_father1)

                            outPutMessages.father_removed_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "remove_grand_father2":

                        outPutMessages.father_remove_requirements()

                        input_remove_grand_father2 = input().split()

                        name_of_grand_father2 = input_remove_grand_father2[0]

                        if type(name_of_mother) == str:

                            controller.remove_grand_father2(name_of_grand_father1)

                            outPutMessages.father_removed_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "insert_grand_mother1":

                        outPutMessages.insert_mother_requirements_message()

                        input_insert_grand_mother1 = input().split()

                        name_of_grand_mother1 = input_insert_grand_mother1[0]

                        place_of_birth = input_insert_grand_mother1[1]

                        Id_of_grand_mother1 = int(input_insert_grand_mother1[2])

                        if type(name_of_grand_mother1) == str and type(place_of_birth) == str and type(
                                Id_of_grand_mother1) == int:

                            controller.insert_grand_mother1(name_of_grand_mother1, place_of_birth, Id_of_grand_mother1)

                            outPutMessages.mother_added_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "insert_grand_mother2":

                        outPutMessages.insert_mother_requirements_message()

                        input_insert_grand_mother2 = input().split()

                        name_of_grand_mother2 = input_insert_grand_mother2[0]

                        place_of_birth = input_insert_grand_mother2[1]

                        Id_of_grand_mother2 = int(input_insert_grand_mother2[2])

                        if type(name_of_grand_mother2) == str and type(place_of_birth) == str and type(
                                Id_of_grand_mother2) == int:

                            controller.insert_grand_mother2(name_of_grand_mother2, place_of_birth, Id_of_grand_mother2)

                            outPutMessages.mother_added_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "remove_grand_mother1":

                        outPutMessages.mother_remove_requirements()

                        input_remove_grand_mother1 = input().split()

                        name_of_grand_mother1 = input_remove_grand_mother1[0]

                        if type(name_of_grand_mother1) == str:

                            controller.remove_grand_mother1(name_of_grand_mother1)

                            outPutMessages.mother_removed_message()

                        else:

                            outPutMessages.invalid_input()

                    elif command == "remove_grand_mother2":

                        outPutMessages.mother_remove_requirements()

                        input_remove_grand_mother2 = input().split()

                        name_of_grand_mother2 = input_remove_grand_mother2[0]

                        if type(name_of_grand_mother2) == str:

                            controller.remove_grand_mother2(name_of_grand_mother1)

                            outPutMessages.mother_removed_message()

                        else:

                            outPutMessages.invalid_input()