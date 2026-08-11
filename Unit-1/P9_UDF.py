# Function without argument

def hello():
    print("Hello Python")

hello()


# Function with argument

def greet(name):
    print("Hello", name)

greet("Hardiksinh")


# Function with multiple arguments

def add(a, b):
    print("Addition:", a + b)

add(10, 20)


# Function with default argument

def student(name, age=18):
    print("Name:", name)
    print("Age:", age)

student("Hardik")
student("Rahul", 20)