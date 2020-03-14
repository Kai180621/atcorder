n = int(input())

ans_list = []
alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

i = 0
while i < n:
  if i == 0:
    ans_list.append(alpha_list[0])
  else:
    new_ans_list = []
    for k in ans_list:
      p = 0
      while p < i + 1:
        new_ans = k + alpha_list[p]
        new_ans_list.append(new_ans)
        print("newanswer:%s" % new_ans_list )
        p += 1
    ans_list = new_ans_list
    print("answer: %s" % ans_list)
  i += 1



print(ans_list)
  