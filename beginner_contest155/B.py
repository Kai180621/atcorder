n = int(input())
alist = list(map(int, input().split()))

ans = "APPROVED"
for a in alist:
  if a % 2 == 0:
    if a % 3 != 0 and a % 5 != 0:
      ans = "DENIED"
      
print(ans)

