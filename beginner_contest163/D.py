import math

n, k = map(int, input().split())
MOD = 1000000007

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))



ans = 0

i = k
while i <= n + 1:
  c = combinations_count(n + 1, i)
  # print(i, c)
  if k % 2 == 0:
    c -= (n + 1) // (2 * i)
  else:
    c -= (n - 1) // (2 * i)
  # print(c)
  ans += c
  i += 1

print(ans % MOD)