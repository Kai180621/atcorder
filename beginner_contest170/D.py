import math

n = int(input())
aes = list(map(int, input().split()))
aes.sort()

ans = [0] * 1100000
for a in aes:
  ans[a] = 1

i = 0
while i < n:
  j = 1
  while j <= math.sqrt(aes[i]):
    if aes[i] % j == 0:
      if ans[j] == 1:
        ans[aes[i]] = 0
        break
      if ans[aes[i] // j] == 1 and aes[i] // j != i:
        
    j += 1
  i += 1

print(sum(ans))


