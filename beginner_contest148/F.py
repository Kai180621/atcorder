n, u, v = map(int, input().split())

branches = [[] for _ in range(100005)]
for _ in range(n - 1):
  a, b = map(int, input().split())
  branches[a].append(b)
  branches[b].append(a)

dist = [-1 for _ in range(100005)]
def dfs(p, d=0, q=-1):
  global dist
  dist[p] = d
  for branch in branches[p]:
    # 親に戻ってくるのを避ける
    if branch == q:
      continue
    dfs(branch, d+1, p)

def calcDist(x):
  global dist
  dist = [-1 for _ in range(100005)]
  dfs(x)
  return dist

udist = calcDist(u)
vdist = calcDist(v)

# print(udist[0:10])
# print(vdist[0:10])

maxdist = 0
for i in range(1, n + 1):
  if udist[i] < vdist[i]:
    maxdist = max(maxdist, vdist[i])

print(maxdist - 1)

