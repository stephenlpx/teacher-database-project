import csv
import pandas

class Staff:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        str = f"Name:{self.name.title()}\nAge:{self.age}\nRole:{self.role.title()}\nDepartment:{self.dept.title()}\n\n"
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

    menu_options = int(input('''
    <<< Welcome >>>
    1: New member
    2:View all staff
    3: Exit
    
    > '''))


    if menu_options == 1:

        staff_type = input("Would you like to add a new member of staff?: ").upper()
        if staff_type == "Y":
            teacher_name = input("Teacher name: ")
            teacher_age = input("Teacher age: ")
            teacher = Teachers(teacher_name, teacher_age)

            f = open("staff-details", "a")
            f.write(f"{teacher.show_details()}")


        elif staff_type == "N":
            print(menu_options)



    elif menu_options == 2:
        file = open("staff-details", "r")
        data = file.read()
        print(f"<<<STAFF LIST>>>\n{data.strip()}")


    elif menu_options == 3:
        is_on = False




