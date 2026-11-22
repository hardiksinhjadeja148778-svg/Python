import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Riya", "Karan", "Neha"],
    "Age": [20, np.nan, 19, 22],
    "Marks": [78, 85, np.nan, np.nan]
}
df = pd.DataFrame(data)

print("Original:\n", df)
print("\nMissing values:\n", df.isnull().sum())

print("\nAfter dropna():\n", df.dropna())

print("\nAfter fillna(0):\n", df.fillna(0))

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
print("\nFilled with mean/median:\n", df)