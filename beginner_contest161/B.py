n, m = map(int, input().split())
a_list = list(map(int, input().split()))

sum_a = sum(a_list)
# print(sum_a)
border = (1 / (4 * m)) * sum_a
# print(border)

count = 0
for a in a_list:
  if a >= border:
    count += 1
# print(count)

if count >= m:
  print("Yes")
else:
  print("No")