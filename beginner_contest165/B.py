x = int(input())

i = 100
k = 1
while i < x:
  i = int(i * 1.01)
  k += 1

print(k - 1)