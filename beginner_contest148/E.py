n = int(input())
ans = 0
if n % 2 != 0:
  print(ans)
else:
  m = n // 2
  e = 1
  while 5 ** e <= m:
    ans += m // (5 ** e)
    e += 1
  print(ans)