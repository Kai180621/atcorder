n, m = map(int, input().split())
aes = list(map(int, input().split()))

aes = sorted(aes, reverse=True)
dps = []

i = 0
while i < n:
  if i == 0:
    dps.append(aes[0] * 2)
  else:
    

    