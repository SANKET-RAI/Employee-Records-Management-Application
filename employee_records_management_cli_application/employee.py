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
            try:
                for p_name in range(0, len(self.project_name)):
                    if p_name == len(self.project_name) - 1:
                        print(self.project_name[p_name] + ".")
                    elif p_name == len(self.project_name) - 2:
                        print(self.project_name[p_name], end=" & ")
                    else:
                        print(self.project_name[p_name], end=", ")

            except:
                print("None")
            print("Skill Sets :", end=" ")

            try:
                for skills in range(0, len(self.skill_set)):
                    if skills == len(self.skill_set) - 1:
                        print(self.skill_set[skills] + ".")
                    elif skills == len(self.skill_set) - 2:
                        print(self.skill_set[skills], end=" & ")
                    else:
                        print(self.skill_set[skills], end=", ")

            except:
                print("None")
        else:
            print("Cannot Display Admin details, it is confidential !")
