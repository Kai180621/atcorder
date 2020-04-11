import queue
INF = 1001001001

h, w = map(int, input().split())
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

ans = 0

maze = []
i = 0
while i < h:
  width = list(input())
  maze.append(width)
  i += 1
print(maze)

for si in range(h):
  for sj in range(w):
    if maze[si][sj] == "#":
      continue
    q = queue.Queue()
    dist = [[INF] * w] * h

    def update(i, j, x):
      global q
      global dist
      if dist[i][j] != INF: return
      dist[i][j] = x
      q.put([i, j])

    update(si, sj, 0)

    while not q.empty():
      current = q.get()
      i = current[0]
      j = current[1]
      for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if ni < 0 or ni > h or nj < 0 or nj > w: continue
        if maze[ni][nj] == "#": continue
        update(ni, nj, dist[i][j] + 1)

    for i in range(h):
      for j in range(w):
        if dist[i][j] == INF: continue
        ans = max(dist[i][j], ans)

    print([si,sj],ans)

    sj += 1
  si += 1

print(ans)