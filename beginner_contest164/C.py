n = int(input())
collections = {}
ans = 0

for _ in range(n):
  s = input()
  collections[s] = 1


print(sum(collections.values()))