n, m = map(int, input().split())
aes = list(map(int, input().split()))

sumcost = 0
for a in aes:
  sumcost += a

if sumcost > n:
  print(-1)
else:
  print(n - sumcost)