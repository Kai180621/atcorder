import copy

h, w, k = map(int, input().split())
cs = []
ans = 0

def count_sharps(tmp):
  sharp = 0
  for y in range(h):
    sharp += tmp[y].count("#")
  if sharp == k:
    return True
  else:
    return False



for _ in range(h):
  cs.append(list(input()))

for i in range(2 ** h):
  for j in range(2 ** w):
    tmp = copy.deepcopy(cs)
    for p in range(h):
      if ((i >> p) & 1):
        for x in range(w):
          tmp[p][x] = "r"
    for q in range(w):
      if ((j >> q) & 1):
        for y in range(h):
          tmp[y][q] = "r"

    if count_sharps(tmp):
      ans += 1

print(ans)