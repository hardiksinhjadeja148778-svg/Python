import re

# Create a sample text file
file = open("details.txt", "w")
file.write("Name: Hardiksinh, Email: hardiksinh.jadeja148778@gmail.com, Phone: 9876543210\n")
file.write("Name: Arjun, Email: arjunpatell5359@gmail.com, Phone: 9123456780\n")
file.close()

# Read the file
file = open("details.txt", "r")
data = file.read()
file.close()

# Extract emails
emails = re.findall(r"[\w\.]+@[\w\.]+", data)

# Extract 10-digit phone numbers
phones = re.findall(r"\d{10}", data)

print("Emails:", emails)
print("Phone Numbers:", phones)