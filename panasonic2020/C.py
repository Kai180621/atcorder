
a, b, c = map(int, input().split())

if a**2 + b**2 + c**2 - 2*a*b - 2*b*c - 2*c*a > 0: 
  print("Yes")
else:
  print("No")