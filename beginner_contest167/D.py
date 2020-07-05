n, k = map(int, input().split())

to = [0]
to += list(map(int, input().split()))

passed = [0] * (n + 1)

circle = [1]
st = -1
while True:
  nx = to[circle[-1]]
  if passed[nx] == 1:
    st = nx
    break
  circle.append(nx)
  passed[nx] = 1
  

l1 = circle.index(st)
l2 = len(circle) - l1

if k < l1:
  print(circle[k])
elif k < l1 + l2:
  print(circle[k])
else:
  div = (k - l1) % l2
  print(circle[l1+div])