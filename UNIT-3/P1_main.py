# Importing the user-defined module

import P1_MainModul

print("Using import P1_MainModul")
print("Addition       =", P1_MainModul.add(10, 5))
print("Subtraction    =", P1_MainModul.sub(10, 5))
print("Multiplication =", P1_MainModul.mul(10, 5))
print("Division       =", P1_MainModul.div(10, 5))

# Another way to import
from P1_MainModul import add, sub

print("\nUsing from ... import")
print("Addition    =", add(20, 10))
print("Subtraction =", sub(20, 10))