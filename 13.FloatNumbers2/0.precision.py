# e 1/0! + 1/1! + 1/2! + 1/3! ...

import math
from math import factorial

precision = float(input("Укажите необходимую точность (1e-20)) \n> "))
result = 0
i = 0
addMember = 1

while addMember > precision:
    addMember = 1 / math.factorial(i)
    result += addMember
    i += 1
print("Результат:", result)
print("Константа:", math.e)
