# Dunder: 

# Standard Employee class 
class Employee:
    # initialization function
    def __init__(self, name, age, position, salary, gender):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.gender = gender

    # readable string function
    def __str__(self):
        return (f"{self.name} is {self.age} years old. Employee is {self.position} with the salary of ${self.salary}")

    # info function
    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is {self.position} with the salary of ${self.salary}")
    
    # less than function to compare salary of employees
    def __lt__(self, other):
        return self.salary < other.salary

def Main():
    # Create an employee object
    emp1 = Employee("Roshan", 45, "Architect", 20000000, "M")
    emp2 = Employee("John", 40, "Architect", 10000000, "M")

    print(emp1)

    if(emp1 > emp2):
        print(f"{emp1.name} has the more salary than {emp2.name}")
    elif(emp1 < emp2):
        print(f"{emp2.name} has the more salary than {emp1.name}")
    else:
        print(f"{emp1.name} and {emp2.name} has the same salary")


Main()



