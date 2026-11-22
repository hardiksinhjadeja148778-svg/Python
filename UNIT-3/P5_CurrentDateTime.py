import datetime

now = datetime.datetime.now()

print("--- Current Date and Time ---")
print("Current Date and Time:", now)
print("Date:", now.date())
print("Time:", now.time())

print("\n--- Separate Parts ---")
print("Year   :", now.year)
print("Month  :", now.month)
print("Day    :", now.day)
print("Hour   :", now.hour)
print("Minute :", now.minute)
print("Second :", now.second)

print("\n--- Formatted Output (strftime) ---")
print("Date format (DD-MM-YYYY):", now.strftime("%d-%m-%Y"))
print("Time format (12 hour)   :", now.strftime("%I:%M:%S %p"))
print("Full format             :", now.strftime("%A, %d %B %Y"))

print("\n--- Using today() ---")
print("Today's date:", datetime.date.today())