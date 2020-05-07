#################
## Objects in Python
#################
2020
3.145
"Hello World"
[3, 2, 1]
{"NY":"New York", "CA": "California"}

#################
## EXAMPLE: Employee
#################

class Employee:
    """ define the properties """
    def __init__(self, name, salary, department=None):
        self.name = name
        self.salary = salary
        self.department = None
    def income_tax(self):
        return self.salary*(0.22)

me = Employee("Kwabena", 50000)
print(me)


#################
## EXAMPLE: Dog class
#################
class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


d = Dog('Fido', 'French Bulldog')
