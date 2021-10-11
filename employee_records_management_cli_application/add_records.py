import json
import view_records


def add():
    file = "data.json"
    with open(file, "r+") as json_file:
        json_data = json.load(json_file)
    json_file.close()
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
    json_data.update({emp_id: [
        {"name": new_name, "user_type": new_user_type, "years_of_experience": new_years_of_experience,
         "joining_date": new_joining_date, "dob": new_dob, "age": new_age, "project_name": new_project_name,
         "skill_set": new_skill_set}]})
    view_records.logging.info('Created New Record With Employee Id : {}, Employee Name : {}, Employee User Type : {}'
                              .format(emp_id, new_name, new_user_type))

    with open(file, "r+") as json_file_new:
        json.dump(json_data, json_file_new, indent=4)
    json_file_new.close()
