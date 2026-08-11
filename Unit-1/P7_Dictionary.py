# Create Dictionary

student = {
    "name": "Hardik",
    "age": 20,
    "course": "Python"
}

print(student)

# Access values
print("Name:", student["name"])

# Dictionary Methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Add new value
student["city"] = "Gujarat"

# Update value
student["age"] = 21

print(student)

# Iteration
for key, value in student.items():
    print(key, ":", value)