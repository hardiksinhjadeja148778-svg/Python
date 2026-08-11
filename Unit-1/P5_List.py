# Create a list
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First 3 elements:", numbers[0:3])

# Add element
numbers.append(60)
print("After append:", numbers)

# Remove element
numbers.remove(20)
print("After remove:", numbers)

# List Comprehension
square = [x * x for x in numbers]
print("Squares:", square)