a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a < b:
  if a + t * v >= b + t * w:
    print("YES")
  else:
    print("NO")
else:
  if a - t * v <= b - t * w:
    print("YES")
  else:
    print("NO")