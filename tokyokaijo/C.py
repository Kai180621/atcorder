n, k = map(int, input().split())
ds = list(map(int, input().split()))

t = 0
while t < k:
  tmpds = [1] * n
  i = 0
  while i < n - 1:
    j = 1
    while j <= ds[i]:
      if i + j > n - 1:
        break 
      tmpds[i + j] += 1
      j += 1
    i += 1

  i = n - 1
  while i > 0:
    j = 1
    while j <= ds[i]:
      if i - j <= 0:
        break
      tmpds[i - j] += 1
      j += 1
    i -= 1

  ds = tmpds.copy()
  if ds.count(n) == n:
    break
  t += 1

dsstr = map(str, ds)
ans = " ".join(dsstr)
print(ans)