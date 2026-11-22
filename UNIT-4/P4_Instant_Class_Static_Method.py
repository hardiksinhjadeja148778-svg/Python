class Student:
    college = "Marwadi University"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show(self):
        print("Instance method: Name is", self.name)

    # Class method
    @classmethod
    def show_college(cls):
        print("Class method: College is", cls.college)

    # Static method
    @staticmethod
    def add(a, b):
        print("Static method: Sum is", a + b)

s = Student("Amit")
s.show()
Student.show_college()
Student.add(10, 20)