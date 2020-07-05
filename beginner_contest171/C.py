import string

n = int(input())


ans = []
while i >= 0:
  q, mod = divmod(n, 26 ** i)
  ans.append(q - 1)
  n = mod
  i -= 1


print(ans)

s = ""
for a in ans:
  s += string.ascii_lowercase[a]
print(s)






