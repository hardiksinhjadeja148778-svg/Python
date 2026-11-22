# Write mode (w) - creates file / overwrites
f = open("data.txt", "w")
f.write("Hello Python\n")
f.write("Welcome to file handling\n")
f.close()

# Append mode (a) - adds at the end
f = open("data.txt", "a")
f.write("This line is appended\n")
f.close()

# Read mode (r)
f = open("data.txt", "r")
print("--- read() ---")
print(f.read())
f.close()

# Read line by line
f = open("data.txt", "r")
print("--- readline() ---")
print(f.readline())
print("--- readlines() ---")
print(f.readlines())
f.close()

# Using with statement (closes the file automatically)
with open("data.txt", "r") as f:
    print("--- with open ---")
    for line in f:
        print(line.strip())