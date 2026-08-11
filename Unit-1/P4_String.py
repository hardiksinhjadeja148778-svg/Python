s = "Python Programming"

# Basic Operations
print("String:", s)
print("Length:", len(s))
print("First character:", s[0])

# Slicing
print("First 6 characters:", s[0:6])
print("Reverse:", s[::-1])

# Formatting
name = "Hardik"
age = 20

print("My name is {} and my age is {}".format(name, age))
print(f"My name is {name} and my age is {age}")

# Built-in String Functions
print(s.upper())
print(s.lower())
print(s.replace("Python", "Java"))
print(s.count("m"))
print(s.find("Programming"))