import view_records
import add_records
import update_records
import delete_records


def choices():
    print()
    print("SELECT THE OPERATION YOU WANT TO PERFORM : ")
    print("(1) - View Employee Records")
    print("(2) - Add Employee Record")
    print("(3) - Update Employee Record")
    print("(4) - Delete Employee Record")
    print("(5) - Exit")


while True:
    choices()
    choice = input("Enter your Choice number : ")
    if choice == '1':
        e_id = input("Please enter employee id : ")
        view_records.view(e_id)
    elif choice == '2':
        add_records.add()
    elif choice == '3':
        e_id = input("Please enter employee id : ")
        update_records.update(e_id)
    elif choice == '4':
        e_id = input("Please enter employee id : ")
        delete_records.delete(e_id)
    elif choice == '5':
        print("Exited Successfully !")
        exit(0)
    else:
        print("Please enter a valid choice number!")
