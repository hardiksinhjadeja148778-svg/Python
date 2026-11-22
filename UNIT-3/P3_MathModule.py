import math

num = int(input("Enter a number: "))

print("\n--- Basic Functions ---")
print("Square root  :", math.sqrt(num))
print("Power (num^2):", math.pow(num, 2))
print("Factorial    :", math.factorial(num))
print("Absolute     :", math.fabs(-num))

print("\n--- Rounding Functions ---")
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.8  :", math.floor(4.8))

print("\n--- Other Functions ---")
print("GCD of 12 and 18 :", math.gcd(12, 18))
print("Log of 100 (base 10):", math.log10(100))
print("Sin(90 degrees)  :", math.sin(math.radians(90)))
print("Cos(0 degrees)   :", math.cos(math.radians(0)))

print("\n--- Constants ---")
print("Value of PI :", math.pi)
print("Value of e  :", math.e)