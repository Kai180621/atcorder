n = int(input())

ans = 0
i = 1
while i <= n:
  if i % 3 == 0 or i % 5 == 0:
    i += 1
    continue
  ans += i
  i += 1

print(ans)