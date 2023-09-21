class MyEmployee:
    pass

e = MyEmployee();
# since class has no attributes, it will print empty dictionary like {}
print(e.__dict__)

# Standard Employee class 
class Employee:
    # initialization function
    def __init__(self, name, age, position, salary, gender):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.gender = gender

    # info function
    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is {self.position} with the salary of ${self.salary}")

    # increase salary by a percentage
    def increaseSalary(self, percent):
        self.salary += self.salary * percent / 100
    
    def decreaseSalary(self, percent):
        NotImplementedError("This method is not implemented yet")

def Main():
    # Create an employee object
    emp1 = Employee("Roshan", 45, "Architect", 10000000, "M")
    emp2 = Employee("John", 40, "Architect", 10000000, "M")

    emp1.info()

    emp1.decreaseSalary(10)


Main()



