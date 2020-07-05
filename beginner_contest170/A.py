xs = map(int, input().split())

for i, x in enumerate(xs):
  if x == 0:
    ans = i + 1

print(ans)
