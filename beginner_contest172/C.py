n, m, k = map(int, input().split())
aes = list(map(int, input().split()))
bs = list(map(int, input().split()))

ans = 0
i = 0
while i <= n:
  suma = k - sum(aes[:i])
  if suma < 0:
    break
  i += 1
  j = m
  while j >= 0:
    sumall = suma - sum(bs[:j])
    if sumall >= 0:
      break
    j -= 1
  
  ans = max(ans, i + j -1)
  # print(i-1, j-1, ans)

print(ans)