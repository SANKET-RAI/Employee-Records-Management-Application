import json
import view_records


def update(emp_id):
    file = "data.json"
    with open(file, "r+") as json_file:
        json_data = json.load(json_file)
    json_file.close()
    if emp_id in json_data:
        temp_emp = json_data[emp_id]
        new_name = input("Enter updated name : ")
        if new_name == "":
            new_name = temp_emp[0]["name"]
        while True:
            new_user_type = input("Enter updated user type : ")
            if new_user_type == "":
                new_user_type = temp_emp[0]["user_type"]
                break
            elif new_user_type.lower() == "admin":
                print("Cannot change user type to admin, please enter user type again !")
            else:
                break
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
        json_data.update({emp_id: [
            {"name": new_name, "user_type": new_user_type, "years_of_experience": new_years_of_experience,
             "joining_date": new_joining_date, "dob": new_dob, "age": new_age, "project_name": new_project_name,
             "skill_set": new_skill_set}]})
        with open(file, "r+") as json_file_new:
            json.dump(json_data, json_file_new, indent=4)
        json_file_new.close()
        view_records.logging.info('Updated Record With Employee Id : {}, Employee Name : {}, Employee User Type : {}'
                                  .format(emp_id, new_name, new_user_type))
    else:
        print("Please enter a valid employee id which exists in the database !")
