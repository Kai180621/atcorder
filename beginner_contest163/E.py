n = int(input())
aes = list(map(int, input().split()))

aes_left = aes[:]

ans = 0
i = 0
while i < n // 2:
  s = n // 2
  maxs = 0
  maxhappys = 0
  while s < n:
    if aes[s] * (s - i) > maxhappys:
      maxhappys = aes[s] * (s - i)
      maxs = s
    s += 1
  aes[maxs] = 0
  ans += maxhappys

  t = 1
  maxt = 0
  maxhappyt = 0
  while t < n // 2 + 1:
    if aes[-t] * (-t - 1) > maxhappyt:
      maxhappyt = aes[t] * (-t -1)
      maxt = t
    t += 1
  aes[maxt] = 0
  ans += maxhappyt

  print(maxhappys, maxhappyt, aes)

  i+= 1
  
print(ans)