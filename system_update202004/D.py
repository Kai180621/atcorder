import math

n, q = map(int, input().split())
alist = list(map(int, input().split()))
slist = list(map(int, input().split()))

a_gcd = []

def binary_search(li, i):
  if math.gcd(li[n - 1], i) != 1:
    return math.gcd(li[n - 1], i)
  if math.gcd(li[0], i) == 1:
    return 1
  ok = 0
  ng = n - 1
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if math.gcd(li[mid], i) != 1:
      ok = mid
    else:
      ng = mid
  return ng + 1  

i = 0
while i < n:
  if i == 0:
    a_gcd.append(alist[0])
    i += 1
    continue
  a_gcd.append(math.gcd(alist[i - 1], alist[i]))
  i += 1

# print(a_gcd)

for s in slist:
  print(binary_search(a_gcd, s))
  
