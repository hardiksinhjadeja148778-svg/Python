import random

low = int(input("Enter starting number: "))
high = int(input("Enter ending number  : "))

print("\n--- Random Numbers ---")
print("Random integer      :", random.randint(low, high))
print("Random number (0-1) :", random.random())
print("Random decimal      :", random.uniform(low, high))
print("Random with step    :", random.randrange(low, high, 2))

print("\n--- Random with List ---")
numbers = [10, 20, 30, 40, 50]
print("Original list  :", numbers)
print("Random choice  :", random.choice(numbers))
print("Random sample  :", random.sample(numbers, 3))

random.shuffle(numbers)
print("After shuffle  :", numbers)