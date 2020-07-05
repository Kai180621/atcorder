MOD = 1000000007

n, k = map(int, input().split())
xs = sorted(list(map(int, input().split())))
minus = []
plus = []

ans = -MOD

for i in range(n):
  if xs[i] >= 0:
    minus = xs[:i]
    plus = sorted(xs[i:], reverse=True)
    break

for i in range(len(plus) + 1):
  tmp = 1
  l = k - i
  if l < 0:
    break
  if l > len(minus):
    continue

  if l % 2 == 0:
    if i != 0:
      for p in plus[:i]:
        tmp *= p
    if l != 0:
      for m in minus[:l]:
        tmp *= m
  else:
    if i != 0:
      for p in plus[len(plus)-i:]:
        tmp *= p
    if l != 0:
      for m in minus[len(minus) - l:]:
        tmp *= m
  
  ans = max(ans, tmp)

print(ans)