a, b, n = map(int, input().split())
x = 0

if n % b == 0:
  x = n - 1
else:
  x = n
ans = (a * x) // b - a * (x // b)
print(ans)