n = int(input())
ss, ts = map(str, input().split())

ans = ""

i = 0
while i < n:
  ans += ss[i]
  ans += ts[i]
  i += 1

print(ans)