n = int(input())
aes = list(map(int, input().split()))

anss = [0] * n

for a in aes:
  anss[a - 1] += 1

for ans in anss:
  print(ans)