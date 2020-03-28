x = int(input())

count_500 = 0
count_5 = 0
while x >= 500:
  x -= 500
  count_500 += 1

while x >= 5:
  x -= 5
  count_5 += 1
  
ans = 1000 * count_500 + 5 * count_5
print(ans)