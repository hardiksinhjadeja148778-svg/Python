import re
import os

# Create a text file with some data
with open("data.txt", "w") as f:
    f.write("Name: hardiksinh, Email: hardiksinhjadeja64@gmail.com, Phone: 8866735353\n")
    f.write("Name: het, Email: het.r@yahoo.com, Phone: 9123456789\n")
    f.write("Date of joining: 12-05-2023 and 25-08-2024\n")

# Read the file
with open("data.txt", "r") as f:
    data = f.read()

# 1. re.match() - checks only the beginning of the text
print("--- re.match() ---")
result = re.match(r"Name", data)
print("Match 'Name' at start :", result.group() if result else "Not found")

result = re.match(r"Email", data)
print("Match 'Email' at start:", result.group() if result else "Not found")

# 2. re.search() - finds the first match anywhere in the text
print("\n--- re.search() ---")
result = re.search(r"[\w\.]+@[\w\.]+\.\w+", data)
print("First email :", result.group() if result else "Not found")

result = re.search(r"\b\d{10}\b", data)
print("First phone :", result.group() if result else "Not found")

# 3. re.findall() - returns all matches as a list
print("\n--- re.findall() ---")
emails = re.findall(r"[\w\.]+@[\w\.]+\.\w+", data)
print("Emails        :", emails)

phones = re.findall(r"\b\d{10}\b", data)
print("Phone numbers :", phones)

dates = re.findall(r"\d{2}-\d{2}-\d{4}", data)
print("Dates         :", dates)

# Delete the file
os.remove("data.txt")