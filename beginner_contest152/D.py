n = int(input())

count = 0
i = 1
while i <= n:
  istr = str(i)
  irev = istr[::-1]
  if irev > n:
    continue
  else:
    if len(istr) == 1:
      
