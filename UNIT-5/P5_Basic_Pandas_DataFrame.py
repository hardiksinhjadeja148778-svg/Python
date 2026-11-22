import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Karan", "Neha", "Raj"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [78, 85, 62, 90, 71]
}
df = pd.DataFrame(data)

print(df)
print("\nFirst 3 rows:\n", df.head(3))
print("\nInfo:")
df.info()
print("\nStatistics:\n", df.describe())
print("\nAverage marks:", df["Marks"].mean())
print("Max marks:", df["Marks"].max())
print("Min marks:", df["Marks"].min())
print("\nStudents with marks > 75:\n", df[df["Marks"] > 75])
print("\nSorted by marks:\n", df.sort_values("Marks", ascending=False))