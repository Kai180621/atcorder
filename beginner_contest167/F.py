n = int(input())

ls = []
rs = []

for _ in range(n):
  s = input()
  lx = 0
  rdiv = 0 
  for kakko in s:
    if kakko == "(":
      rdiv += 1
    else:
      if rdiv == 0:
        lx += 1
      else:
        rdiv -= 1

  rx = 0
  ldiv = 0
  for kakko in s[::-1]:
    if kakko == ")":
      ldiv += 1
    else:
      if ldiv == 0:
        rx += 1
      else:
        ldiv -= 1
  
  ls.append(lx)
  rs.append(rx)


