a, b, c = map(int, input().split())

if a == b:
  if b == c:
    print("No")
  else:
    print("Yes")
else:
  if b == c:
    print("Yes")
  elif a == c:
    print("Yes")
  else:
    print("No")