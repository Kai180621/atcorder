n = int(input())
aes = list(map(int, input().split()))

current = 1
ans = 0
if not 1 in aes:
  print(-1)
else:
  for a in aes:
    if a == current:
      current += 1
    else:
      ans += 1

  print(ans)
  