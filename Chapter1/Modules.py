import math
from math import sqrt
import cmath

print("Module math imported")
print(math.floor(32.9))

print(int(32.9))

print(math.ceil(32.3))
print(math.ceil(32))


print(sqrt(9))
print(sqrt(2))

#cmath and Complex Numbers
##print(sqrt(-1)) This will trigger a ValueError: math domain error

print(cmath.sqrt(-1))
print((1+3j)*(9+4j))
