class Student:
    roll_num = 101
    name = "Joseph"

    def display(self):
        print("Roll No:", self.roll_num)
        print("Name:", self.name)

obj = Student()
print(obj.roll_num)
print(obj.name)
obj.display()