class Staff:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        str = f"name:{self.name}\nAge:{self.age}\nRole:{self.role}\nDepartment:{self.dept}\n\n"
        return str


class Teachers(Staff):
    teacher_list = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(role=input("What role:"), dept=input("What dept?: "), salary=input("What salary?: "))
        Teachers.teacher_list.append(self)



is_on = True

while is_on:
    staff_type = input("Would you like to add a new member of staff?: ").upper()
    if staff_type == "Y":
        teacher_name = input("Teacher name: ")
        teacher_age = input("Teacher age: ")
        teacher = Teachers(teacher_name, teacher_age)

        f = open("staff-details", "a")
        f.write(f"{teacher.show_details()}")


    elif staff_type == "N":
        is_on = False




