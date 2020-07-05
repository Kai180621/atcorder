k = int(input())
a, b = map(int, input().split())

ans = "NG"
i = a
while i <= b:
  if i % k == 0:
    ans = "OK"
    break
  i += 1

print(ans)