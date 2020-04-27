n, m, s = map(int, input().split())

lines = []
to = [[] for _ in range(n)]

dps = [[] for _ in range(n)]
dps[0].append(0)

for _ in range(m):
  line = list(map(int, input().split()))
  to[line[0]].append(line[1])
  to[line[1]].append(line[0])
  lines.append(line)


citys = []
for _ in range(n):
  city = list(map(int, input().split()))
  citys.append(city)

def dp(i, sv = s):
  global dps
  for t in to[i]:
    



i = 1
while i < n:
  print(dp(i))