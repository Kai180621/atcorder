n = int(input())
ss = list(input())

rcount = 0
gcount = 0
bcount = 0

for s in ss:
  if s == "R":
    rcount += 1
  elif s == "G":
    gcount += 1
  else:
    bcount += 1

sumcount = rcount * gcount * bcount
# print(sumcount)

dist = 1
while dist <= (n - 1) / 2:
  i = 0
  while i + 2 * dist < n:
    if ss[i] != ss[i + dist] and ss[i + dist] != ss[i + 2 * dist] and ss[i + 2 * dist] != ss[i]:
      sumcount -= 1
      # print(ss[i], ss[i+dist], ss[i+dist*2])
    i += 1
  dist += 1

print(sumcount)
    