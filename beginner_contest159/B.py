s = input()
n = len(s)
head_n = int((n-1)/2)
head_s = s[:head_n]
# print(head_s)
foot_n = int((n + 3) / 2 -1)
foot_s = s[foot_n:]
# print(foot_s)

if s == s[::-1] and head_s == head_s[::-1] and foot_s == foot_s[::-1]:
  print("Yes")
else:
  print("No")