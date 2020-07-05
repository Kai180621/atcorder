n, m = map(int, input().split())

to = [[] for _ in range(110000)]
ans = [0] * 110000
queue = []
passed = [0] * 110000
passed[1] = 1

def search(i):
  global queue
  global passed
  global ans
  for j in to[i]:
    if passed[j] == 0:
      queue.append(j)
      passed[j] = 1
      ans[j] = i
  


for _ in range(m):
  a, b = map(int, input().split())
  to[a].append(b)
  to[b].append(a)

search(1)
queue.append(1)

while queue:
  que = queue.pop(0)
  search(que)


print("Yes")
for i in ans[2:n + 1]:
  print(i)