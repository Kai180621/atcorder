n = int(input())
aes = list(map(int, input().split()))

ans = 1

if 0 in aes:
  print(0)
else:
  for a in aes:
    ans *= a
    if ans > 10 ** 18:
      ans = -1
      break
  print(ans)