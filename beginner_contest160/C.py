k, n = map(int, input().split())
a_list = list(map(int, input().split()))

max_dis = 0
sum_dis = 0
i = 0
while i < n:
  if i + 1 == n:
    dis = k - a_list[i] + a_list[0]
    # print(dis)
  else:
    dis = a_list[i + 1] - a_list[i]
    # print(dis)
  sum_dis += dis
  if max_dis < dis:
    # print(i)
    max_dis = dis
  i += 1

# print(max_dis, sum_dis)
print(sum_dis - max_dis)
