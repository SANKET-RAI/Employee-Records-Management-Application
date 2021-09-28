import json

file = "data.json"
with open(file, "r+") as json_file:
    json_data = json.load(json_file)


class Employee:
    def __init__(self, name, user_type, years_of_experience, joining_date, dob, age, project_name, skill_set):
        self.name = name
        self.user_type = user_type
        self.years_of_experience = years_of_experience
        self.joining_date = joining_date
        self.dob = dob
        self.age = age
        self.project_name = project_name
        self.skill_set = skill_set

    def get_details(self):
        l_user_type = self.user_type
        if l_user_type.lower() != "admin":
            print()
            print("Name :", self.name)
            print("User Type :", self.user_type)
            print("Years of Experience :", self.years_of_experience)
            print("Joining Date :", self.joining_date)
            print("Date of Birth :", self.dob)
            print("Age :", self.age)
            print("Project Names :", end=" ")
            for p_name in range(0, len(self.project_name)):
                if p_name == len(self.project_name) - 1:
                    print(self.project_name[p_name] + ".")
                elif p_name == len(self.project_name) - 2:
                    print(self.project_name[p_name], end=" & ")
                else:
                    print(self.project_name[p_name], end=", ")
            print("Skill Sets :", end=" ")
            for skills in range(0, len(self.skill_set)):
                if skills == len(self.skill_set) - 1:
                    print(self.skill_set[skills] + ".")
                elif skills == len(self.skill_set) - 2:
                    print(self.skill_set[skills], end=" & ")
                else:
                    print(self.skill_set[skills], end=", ")
        else:
            print("Cannot Display Admin details, it is confidential !")


def view(emp_id):
    if emp_id in json_data:
        temp_emp = json_data[emp_id]
        te = Employee(temp_emp[0]["name"], temp_emp[0]["user_type"], temp_emp[0]["years_of_experience"], temp_emp[0]["joining_date"], temp_emp[0]["dob"], temp_emp[0]["age"], temp_emp[0]["project_name"], temp_emp[0]["skill_set"])
        te.get_details()
    else:
        print("Please enter a valid employee id which exists in the database !")


def add():
    while True:
        emp_id = input("Please enter a unique new employee id : ")
        if emp_id == "":
            print("Please enter employee id, it is mandatory !")
            continue
        elif emp_id in json_data:
            print("This employee id already exists in database please enter a unique employee id !")
            continue
        else:
            break
    while True:
        new_name = input("Enter new employee's name : ")
        if new_name == "":
            print("Please enter employee name corresponding to employee id :", emp_id, "it is mandatory !")
            continue
        else:
            break
    while True:
        new_user_type = input("Enter new employee's user type : ")
        if new_user_type == "":
            print("Please enter employee user type corresponding to employee id :", emp_id, "it is mandatory !")
            continue
        elif new_user_type.lower() == "admin":
            print("Cannot enter admin as user type corresponding to employee id :", emp_id, "Please change user type !")
            continue
        else:
            break
    temp_years_of_experience = input("Enter new employee's years of experience : ")
    if temp_years_of_experience == "":
        new_years_of_experience = None
    else:
        new_years_of_experience = int(temp_years_of_experience)
    new_joining_date = input("Enter new employee's joining date : ")
    if new_joining_date == "":
        new_joining_date = None
    new_dob = input("Enter new employee's date of birth : ")
    if new_dob == "":
        new_dob = None
    temp_age = input("Enter new employee's age : ")
    if temp_age == "":
        new_age = None
    else:
        new_age = int(temp_age)
    project_names = input("Enter new employee's project names separated by commas : ")
    if project_names == "":
        new_project_name = None
    else:
        new_project_name = list(map(str, project_names.split(",")))
    skill_sets = input("Enter new employee's skill sets separated by commas : ")
    if skill_sets == "":
        new_skill_set = None
    else:
        new_skill_set = list(map(str, skill_sets.split(",")))
    json_data.update({emp_id: [{"name": new_name, "user_type": new_user_type, "years_of_experience": new_years_of_experience, "joining_date": new_joining_date, "dob": new_dob, "age": new_age, "project_name": new_project_name, "skill_set": new_skill_set}]})
    with open(file, "r+") as json_file:
        json.dump(json_data, json_file, indent=4)


def update(emp_id):
    if emp_id in json_data:
        temp_emp = json_data[emp_id]
        new_name = input("Enter updated name : ")
        if new_name == "":
            new_name = temp_emp[0]["name"]
        new_user_type = input("Enter updated user type : ")
        if new_user_type == "":
            new_user_type = temp_emp[0]["user_type"]
        temp_new_years_of_experience = input("Enter updated years of experience : ")
        if temp_new_years_of_experience == "":
            new_years_of_experience = temp_emp[0]["years_of_experience"]
        else:
            new_years_of_experience = int(temp_new_years_of_experience)
        new_joining_date = input("Enter updated joining date : ")
        if new_joining_date == "":
            new_joining_date = temp_emp[0]["joining_date"]
        new_dob = input("Enter updated date of birth : ")
        if new_dob == "":
            new_dob = temp_emp[0]["dob"]
        temp_new_age = input("Enter updated age : ")
        if temp_new_age == "":
            new_age = temp_emp[0]["age"]
        else:
            new_age = int(temp_new_age)
        project_names = input("Enter updated project names separated by commas : ")
        if project_names == "":
            new_project_name = temp_emp[0]["project_name"]
        else:
            new_project_name = list(map(str, project_names.split(",")))
        skill_sets = input("Enter updated skill sets separated by commas : ")
        if skill_sets == "":
            new_skill_set = temp_emp[0]["skill_set"]
        else:
            new_skill_set = list(map(str, skill_sets.split(",")))
        json_data.update({emp_id: [{"name": new_name, "user_type": new_user_type, "years_of_experience": new_years_of_experience, "joining_date": new_joining_date, "dob": new_dob, "age": new_age, "project_name": new_project_name, "skill_set": new_skill_set}]})
        with open(file, "r+") as json_file:
            json.dump(json_data, json_file, indent=4)
    else:
        print("Please enter a valid employee id which exists in the database !")


def delete(emp_id):
    if emp_id in json_data:
        print("Employee details corresponding to employee id :", emp_id, "deleted successfully !")
        del json_data[emp_id]
        with open(file, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
    else:
        print("Please enter a valid employee id which exists in the database !")


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
        view(e_id)
    elif choice == '2':
        add()
    elif choice == '3':
        e_id = input("Please enter employee id : ")
        update(e_id)
    elif choice == '4':
        e_id = input("Please enter employee id : ")
        delete(e_id)
    elif choice == '5':
        print("Exited Successfully !")
        exit(0)
    else:
        print("Please enter a valid choice number!")
