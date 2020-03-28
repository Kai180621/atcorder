n, x, y = map(int, input().split())

xline = x - 1
yline = n - y

yx = y + x


if yx % 2 == 0:
  p = int(yx / 2 - 1)
else:
  p = int(yx / 2)
