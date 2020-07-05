x, n = map(int, input().split())
ps = list(map(int, input().split()))

i = 0
while True:
  if not (x - i) in ps:
    print(x - i)
    break
  if not (x + i) in ps:
    print(x + i)
    break
  i += 1

