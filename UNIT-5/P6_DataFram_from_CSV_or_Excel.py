import pandas as pd

# Create a sample CSV first
pd.DataFrame({
    "Name": ["Amit", "Riya", "Karan"],
    "Marks": [78, 85, 62]
}).to_csv("students.csv", index=False)

# Read CSV
df = pd.read_csv("students.csv")
print("From CSV:\n", df)

df.to_excel("students.xlsx", index=False)
df2 = pd.read_excel("students.xlsx")
print("\nFrom Excel:\n", df2)