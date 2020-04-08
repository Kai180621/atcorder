n = int(input())
ps = list(map(int, input().split()))

ans = 0

i = 0
while i < n:
  if i == 0:
    min_n = ps[0]
    ans += 1
  else:
    if min_n >= ps[i]:
      min_n = ps[i]
      ans += 1
  i += 1

print(ans)
