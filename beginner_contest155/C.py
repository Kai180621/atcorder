n = int(input())
s_list = [input() for i in range(n)]


ans_list = {}
count = 0
for s in s_list:
  s_count = s_list.count(s)
  ans_list[s] = s_count

  # # print(s_count)
  # if s_count > count:
  #   ans_list.clear()
  #   ans_list.append(s)
  #   # print(ans_list)
  #   count = s_count
  # elif s_count == count:
  #   ans_list.append(s)

# print(ans_list)

ans_list = [kv[0] for kv in ans_list.items() if kv[1] == max(ans_list.values())]
# print(max_ans_list)
    
ans_list = sorted(ans_list)
# print(ans_list)

for ans in ans_list:
  print(ans)

