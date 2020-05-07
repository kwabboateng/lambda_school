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
        self.department = department
    def income_tax(self):
        if self.salary <= 9700:
            return self.salary*(0.10)
        elif self.salary <= 39475:
            return self.salary*(0.12)
        elif self.salary <= 84200:
            return self.salary*(0.22)
    def hourly_rate(self):
        return self.salary / (40*50)
    def __str__(self):
        return "{ name: " + self.name + ", " + "salary: " + str(self.salary) + ", " + "department: " + str(self.department) + " }"

me = Employee("Kwabena", 50000, "Product Management")
print(me)
print(me.name)
print(me.salary)


#################
## EXAMPLE: Dog class
#################
class Dog:

    taxonomy = "canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


d = Dog('Fido', 'French Bulldog')
