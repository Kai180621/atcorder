import math

a, b = map(float, input().split())
a = int(a)
b *= 100

ans = math.floor(a * b)

print(int(ans))