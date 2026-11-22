class Employee:
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("Constructor called for", self.name)

    def display(self):
        print("ID:", self.id, "Name:", self.name)

    # Destructor
    def __del__(self):
        print("Destructor called for", self.name)

emp1 = Employee("John", 101)
emp2 = Employee("David", 102)
emp1.display()
emp2.display()

del emp1
print("End of program")