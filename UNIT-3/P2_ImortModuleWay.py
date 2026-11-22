# 1. Import complete module
import math
print("1. import math              :", math.sqrt(25))

# 2. Import specific function
from math import factorial
print("2. from math import        :", factorial(5))

# 3. Import with alias
import math as m
print("3. import math as m        :", m.pow(2, 3))

# 4. Import multiple functions
from math import sqrt, pi
print("4. import multiple         :", sqrt(49), pi)

# 5. Import function with alias
from math import factorial as fact
print("5. function with alias     :", fact(4))

# 6. Import everything
from math import *
print("6. from math import *      :", sqrt(16))