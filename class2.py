# create a class with constructor
class Employee:
    # init is a constructor in python class
    def __init__(self, name, age, salary, gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_details(self):
        print("Name of Employee is", self.name) 
        print("Age of Employee is", self.age) 
        print("Salary of Employee is", self.salary)
        print("Gender of Employee is", self.gender)
# initiating an object
e1=Employee('Debi',21,40000,'Male')
print(e1.employee_details())
e2=Employee('Unknown',21,30000,'Female')
print(e2.employee_details())