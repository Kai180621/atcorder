import math

a, b, h, m = map(int, input().split())

degh = (h * 30) + (30 * m / 60)
degm = 6 * m

deg = math.radians(min(abs(degh - degm), 360 - abs(degh - degm)))

# print(degh, degm, deg)

c2 = a ** 2 + b ** 2 - (2 * a * b * math.cos(deg))
c = math.sqrt(c2)

print(c)