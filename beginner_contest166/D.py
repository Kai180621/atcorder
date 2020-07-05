import sys
x = int(input())

a = 0
while a < 1000:
  b = -1000
  while b < 1000:
    if a ** 5 - b ** 5 == x:
      print(a, b)
      sys.exit()
    b += 1
  a += 1