n = int(input())
ss = input()

ans = 0

i = 0
while i < n-2:
  if ss[i] == "A" and ss[i + 1] == "B" and ss[i + 2] == "C":
    ans += 1
  i += 1
    
print(ans)