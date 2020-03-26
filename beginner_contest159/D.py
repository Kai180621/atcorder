import collections

n = int(input())
a_list = list(map(int, input().split()))
a_counter = collections.Counter(a_list)

# print(a_counter)

sum = 0
for value in a_counter.values():
  if value == 1:
    continue
  sum += int(value * (value - 1) / 2)
  
# print(sum)

ans = 0
for a in a_list:
  ans = sum - (a_counter[a] - 1)
  print(ans)