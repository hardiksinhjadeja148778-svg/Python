# Syntax error (uncomment to see): print("Hello"

# Runtime errors (exceptions)
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

try:
    print(int("abc"))
except ValueError as e:
    print("ValueError:", e)

try:
    a = [1, 2, 3]
    print(a[5])
except IndexError as e:
    print("IndexError:", e)

try:
    print(x)
except NameError as e:
    print("NameError:", e)

try:
    print("5" + 5)
except TypeError as e:
    print("TypeError:", e)

try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print("KeyError:", e)

# Logical error: runs without crashing but gives a wrong answer
a, b = 10, 20
print("Average (wrong):", a + b / 2)