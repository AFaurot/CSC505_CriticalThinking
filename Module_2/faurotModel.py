class FaurotModel:

    # Constructor with initial values.
    def __init__(self, process_phase="none"):
        self.process_phase = process_phase
        # Underscore in list variables is to show that these are softly enforced private variables
        self._communication_list = ["Project Initiation", "Requirements Gathering",
                                    "Feedback", "Deliverable acceptance"]
        self._planning_list = ["Estimating", "Scheduling", "Tracking",
                               "Define Test Cases"]
        self._construction_list = ["Code", "Test", "Peer Validation"]
        self._modeling_list = ["Analysis", "Design"]
        self._deployment_list = ["Delivery", "Support", "TAM"]

    # Class function to print process lists
    def print_lists(self):
        if self.process_phase == "Communication":
            print("The elements of {} are :".format(self.process_phase))
            for process in self._communication_list:
                print(process)
            print("NOTE: {} is part of the process loop".format(self.process_phase))
        elif self.process_phase == "Planning":
            print("The elements of {} are :".format(self.process_phase))
            for process in self._planning_list:
                print(process)
            print("NOTE: {} is part of the process loop".format(self.process_phase))
        elif self.process_phase == "Construction":
            print("The elements of {} are :".format(self.process_phase))
            for process in self._construction_list:
                print(process)
            print("NOTE: {} is part of the process loop".format(self.process_phase))
        elif self.process_phase == "Modeling":
            print("The elements of {} are :".format(self.process_phase))
            for process in self._modeling_list:
                print(process)
            print("NOTE: {} is part of the process loop".format(self.process_phase))
        elif self.process_phase == "Deployment":
            print("The elements of {} are :".format(self.process_phase))
            for process in self._deployment_list:
                print(process)
            print("NOTE: {} is the product of the process loop".format(self.process_phase))
        else:
            print("Invalid process chosen")
        print("")


# Print menu function to reduce amount of code used for printing the menu
def print_menu():
    print("\n----MENU---- \n1 = Print communication elements"
          "\n2 = Print planning elements")
    print("3 = Print construction elements \n4 = Print modeling elements")
    print("5 = Print deployment elements \nq = Quit \nm = Print this menu\n")


def main():

    print("This program will print elements of the Faurot model:\n"
          "----THE FAUROT MODEL----\n")
    print_menu()
    command = input("Enter Command: ")
    #Loop to keep running until q is pressed
    while command != 'q':
        if command == '1':
            process_name = FaurotModel("Communication")
            process_name.print_lists()
        elif command == '2':
            process_name = FaurotModel("Planning")
            process_name.print_lists()
        elif command == '3':
            process_name = FaurotModel("Construction")
            process_name.print_lists()
        elif command == '4':
            process_name = FaurotModel("Modeling")
            process_name.print_lists()
        elif command == '5':
            process_name = FaurotModel("Deployment")
            process_name.print_lists()
        elif command == 'm':
            print_menu()
        else:
            print("Invalid command, make sure there are no whitespaces after your input\n")
        command = input("Enter next command (m for the command menu): ")


if __name__ == '__main__': main()
