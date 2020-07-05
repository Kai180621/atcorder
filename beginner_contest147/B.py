s = input()

l = len(s) // 2
ans = 0
i = 0
while i < l:
  if not s[i] == s[-(i + 1)]:
    ans += 1
  i += 1

print(ans)