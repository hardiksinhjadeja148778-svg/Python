class Student:
    college = "Marwadi University"      # class variable (shared by all objects)

    def __init__(self, name, marks):
        self.name = name                # instance variable (different for each object)
        self.marks = marks

    def display(self):
        print(self.name, self.marks, Student.college)

s1 = Student("Ansh", 78)
s2 = Student("Hardiksinh", 85)
s1.display()
s2.display()

# Changing the class variable affects all objects
Student.college = "MU"
s1.display()
s2.display()

# Changing an instance variable affects only that object
s1.marks = 90
print(s1.marks, s2.marks)