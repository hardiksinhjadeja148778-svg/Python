import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

plt.figure(figsize=(10, 8))

# Line chart
plt.subplot(2, 2, 1)
plt.plot(x, y, marker="o")
plt.title("Line Chart")

# Bar chart
plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C", "D", "E"], y, color="green")
plt.title("Bar Chart")

# Histogram
plt.subplot(2, 2, 3)
marks = [35, 40, 45, 45, 50, 55, 60, 60, 60, 70, 75, 80, 85, 90]
plt.hist(marks, bins=5, color="orange", edgecolor="black")
plt.title("Histogram")

# Pie chart
plt.subplot(2, 2, 4)
plt.pie([40, 30, 20, 10], labels=["Python", "Java", "C", "SQL"], autopct="%1.1f%%")
plt.title("Pie Chart")

plt.tight_layout()
plt.show()