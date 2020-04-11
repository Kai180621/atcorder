n, m = map(int, input().split())

submits = []
for _ in range(m):
  p, s = map(str, input().split())
  p = int(p)
  submits.append([p, s])
  
wrongs = [0] * n
accepteds = [0] * n

i = 0
while i < m:
  order = submits[i][0]
  if submits[i][1] == "AC":
    if accepteds[order] == 0:
      accepteds[order] += 1
  else:
    if accepteds[order] == 0:
      wrongs[order] += 1
  i += 1

print(sum(accepteds), sum(wrongs))