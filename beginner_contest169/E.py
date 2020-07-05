n = int(input())

rs = []
aes = []
bs = []

for _ in range(n):
  a, b = map(int, input().split())
  rs.append([a,b])
  aes.append(a)
  bs.append(b)


aes.sort()
bs.sort(reverse=True)

if n % 2 == 1:
  p = aes[(n - 1) // 2]
  q = bs[(n - 1) // 2]
  ans = q - p + 1
else:
  p1 = aes[n // 2 - 1]
  p2 = bs[n // 2]
  q1 = aes[n // 2]
  q2 = bs[n // 2 - 1]
  ans = (p2 - p1 + 1) + (q2- q1 + 1) - 1
 
# print(p1, p2, q1, q2)
print(ans)