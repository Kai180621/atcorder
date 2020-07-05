n = int(input())

people = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
  a = int(input())
  for _ in range(a):
    x, y = map(int, input().split())
    people[i + 1][x] = y

