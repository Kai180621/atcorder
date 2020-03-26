import collections

n = int(input())
a_list = list(map(int, input().split()))

a_counter = collections.Counter(a_list)

ans = "YES"
for value in a_counter.values():
  if value > 1:
    ans = "NO"
    break

print(ans)