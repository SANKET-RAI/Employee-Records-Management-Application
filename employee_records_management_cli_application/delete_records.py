import json
import view_records


def delete(emp_id):
    file = "data.json"
    with open(file, "r+") as json_file:
        json_data = json.load(json_file)
    json_file.close()
    if emp_id in json_data:
        if json_data[emp_id][0]["user_type"].lower() == "admin":
            print("Cannot delete admin user !")
        else:
            print("Employee details corresponding to employee id :", emp_id, "deleted successfully !")
            view_records.logging.info('Deleted Record With Employee Id : {}, Employee Name : {}, Employee User Type : '
                                      '{}'.format(emp_id, json_data[emp_id][0]["name"],
                                                  json_data[emp_id][0]["user_type"]))
            del json_data[emp_id]
            with open(file, "w") as json_file_new:
                json.dump(json_data, json_file_new, indent=4)
            json_file_new.close()
    else:
        print("Please enter a valid employee id which exists in the database !")
