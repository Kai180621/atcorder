import sys
import fractions
from functools import reduce

n, m = map(int, input().split())
aes = list(map(int, input().split()))

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

halfas = []
for a in aes:
  if a % 2 != 0:
    print(0)
    sys.exit()
  halfas.append(a // 2)
  
lcm = lcm_list(halfas)
# print(lcm)
pp = m // lcm
if pp % 2 == 0:
  ans = int(pp / 2)
else: 
  ans = int((pp + 1) / 2)


print(ans)

