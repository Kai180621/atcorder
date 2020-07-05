n, k = map(int, input().split())

sumans = [0] * 110

i = 1
while i <= k:
  d = int(input())
  j = 0
  aes = list(map(int, input().split()))
  while j < d:
    sumans[aes[j]] = 1
    j += 1
  i += 1

ans = n - sum(sumans)
print(ans)