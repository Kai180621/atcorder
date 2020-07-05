n = int(input())
aes = list(map(int, input().split()))
q = int(input())
bs = []
cs = []
for _ in range(q):
  b,c = map(int, input().split())
  bs.append(b)
  cs.append(c)


counts = [0] * 110000

for a in aes:
  counts[a] += 1

ans = 0
for i, c in enumerate(counts):
  ans += i * c

for i in range(q):
  p = counts[bs[i]]
  counts[bs[i]] = 0
  ans -= bs[i] * p
  counts[cs[i]] += p
  ans += cs[i] * p
  print(ans)

