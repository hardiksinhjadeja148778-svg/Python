def divide(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b

print(divide(10, 2))

try:
    print(divide(10, 0))
except AssertionError as e:
    print("AssertionError:", e)

marks = 85
assert marks >= 35, "Student failed"
print("Student passed")