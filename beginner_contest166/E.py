n = int(input())
aes = list(map(int, input().split()))
ans = 0
sums = []

sums.append(aes[0])

i = 1
while i < n:
  sums.append(sums[i - 1] + aes[i])
  
for i, s in enumerate(sums):
  

print(ans)