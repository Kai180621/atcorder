a, b = map(int, input().split())

astr = str(a) * b
bstr = str(b) * a

if astr < bstr:
  print(astr)
else:
  print(bstr)