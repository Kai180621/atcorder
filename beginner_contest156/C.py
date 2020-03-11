n = int(input())
xs = list(map(int, input().split()))

# print(n, x)

ans = 1000000000000
i = 0
while i < 100:
  sum = 0
  for x in xs:
    sum += (x - i)**2
  if sum < ans:
    ans = sum
  i += 1

print(ans)
