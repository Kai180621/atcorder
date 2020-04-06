import math

n, q = map(int, input().split())
alist = list(map(int, input().split()))
slist = list(map(int, input().split()))

for s in slist:
  x = s
  for j, a in enumerate(alist):
    x = math.gcd(x, a)
    if x == 1:
      print(j+1)
      break
  else:
    print(x)

