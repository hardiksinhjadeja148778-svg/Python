import re

text = "My phone number is 9876543210"

# 1. re.search() - finds the first match anywhere in the text
print("--- re.search() ---")
result = re.search(r"\d+", text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")

# 2. re.match() - matches only at the beginning of the text
print("\n--- re.match() ---")
print("Match 'My'    :", re.match(r"My", text))
print("Match 'phone' :", re.match(r"phone", text))

# 3. re.findall() - returns all matches as a list
print("\n--- re.findall() ---")
data = "Call 9876543210 or 9123456789 today"
print("All numbers   :", re.findall(r"\d{10}", data))
print("All words     :", re.findall(r"\w+", "Python is fun"))
print("Capital letters:", re.findall(r"[A-Z]", "Hello World Python"))

# 4. re.sub() - replaces matches
print("\n--- re.sub() ---")
print("Replaced      :", re.sub(r"\d+", "XXXXXXXXXX", text))

# 5. re.split() - splits the text at matches
print("\n--- re.split() ---")
print("Split         :", re.split(r"\s", "Python is easy"))