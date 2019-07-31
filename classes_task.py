

class Employee(object):

    def __init__(self, name, age, salary, employment_date):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_date = employment_date

    def get_working_years(self):
        return 2019 - int(self.employment_date)
    def __repr__(self):
        return "name: {}, age: {}, salary: {}, working years: {}\n".format(self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):

    def __init__(self, name, age, salary, employment_date, bonus_percentage):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_date = employment_date
        self.bonus_percentage = bonus_percentage
    def get_bonus(self):
        return float(self.bonus_percentage) * float(self.salary)
    def __repr__(self):
        return "name: {}, age: {}, salary: {}, working years: {}, bonus: {}\n".format(self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())


employees = []
managers = []
choice = 1

print("Welcome to HR Pro 2019")
while choice != "5":
    print("Choose an action to do:")
    print("""1. show employees
2. show managers
3. add an employee
4. add a manager
5. exit""")
    choice = input("What would you like to do? ")
    
    if len(choice) != 1 or choice not in "12345":
        print("Invalid input. Please try again")
        continue

    if choice == "1":
        if len(employees) > 0:
            print("Employees:")
            for emp in employees:
                print(emp)
        else:
            print("We don't have employees!\n")
    elif choice == "2":
        if len(managers) > 0:
            print("Managers:")
            for man in managers:
                print(man)
        else:
            print("We don't have managers!\n")
    elif choice == "3":
        print("-"*20)
        name = input("name: ")
        age = input("age: ")
        salary = input("salary: ")
        emp_year = input("employment year: ")

        employees.append(Employee(name, age, salary, emp_year))
        print("Employee added successfully")
    elif choice == "4":
        print("-"*20)
        name = input("name: ")
        age = input("age: ")
        salary = input("salary: ")
        emp_year = input("employment year: ")
        bonus_p = input("bonus percentage: ")

        managers.append(Manager(name, age, salary, emp_year, bonus_p))
        print("Manager added successfully")
        
    
