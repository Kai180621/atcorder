import math
from functools import reduce
import time
# 処理前の時刻
t1 = time.time()

def gcd(*numbers):
    return reduce(math.gcd, numbers)


k = int(input())

ans = 0
a = 1
while a <= k:
  b = a
  while b <= k:
    c = b
    while c <= k:
      if a == b and b == c:
        ans += gcd(a, b, c)
      elif a == b or b == c or c == a:
        ans += 3 * gcd(a, b, c)
      else:
        ans += 6 * gcd(a, b, c)
      c += 1
    b += 1
  a += 1
         
print(ans)


 
 
# 処理後の時刻
t2 = time.time()
 
# 経過時間を表示
elapsed_time = t2-t1
print(f"経過時間：{elapsed_time}")