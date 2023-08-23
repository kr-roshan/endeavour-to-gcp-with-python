# Create an employee class 
class Employee:
    def __init__(self, name, age, position, salary, gender):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.gender = gender

    def __str__(self):
        return (f"{self.name} is {self.age} years old. Employee is {self.position} with the salary of ${self.salary}")

    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is {self.position} with the salary of ${self.salary}")

def Main():
    # Create an employee object
    emp1 = Employee("Roshan", 45, "Architect", 10000000, "M")
    # Print the employee's name
    print(emp1)
    print(emp1.info())

Main()