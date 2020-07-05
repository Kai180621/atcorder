n = int(input())

ans = 0
p = 1
while p <= n:
  c = n // p
  q = p * c
  ans += (p + q) * c // 2
  p += 1
  
print(ans)
    