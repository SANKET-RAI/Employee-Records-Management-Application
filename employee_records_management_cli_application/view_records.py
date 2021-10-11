import json
import logging
import employee


logging.basicConfig(filename='employee_information.log', level=logging.INFO, format='%(asctime)s : %(message)s')


def view(emp_id):
    new_file = "data.json"
    with open(new_file, "r+") as json_file:
        json_data = json.load(json_file)
    json_file.close()
    if emp_id in json_data:
        temp_emp = json_data[emp_id]
        te = employee.Employee(temp_emp[0]["name"], temp_emp[0]["user_type"], temp_emp[0]["years_of_experience"],
                               temp_emp[0]["joining_date"], temp_emp[0]["dob"], temp_emp[0]["age"],
                               temp_emp[0]["project_name"], temp_emp[0]["skill_set"])
        te.get_details()
        logging.info('Fetched Records of Employee Id : {}, Employee Name : {}, Employee User Type : {}'
                     .format(emp_id, temp_emp[0]["name"], temp_emp[0]["user_type"]))
    else:
        print("Please enter a valid employee id which exists in the database !")
