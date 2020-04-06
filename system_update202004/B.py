n = int(input())

rballs = []
bballs = []
for _ in range(n):
  number, color = map(str, input().split())
  number = int(number)
  if color == "R":
    rballs.append(number)
  else:
    bballs.append(number)

# print(rballs, bballs)

rballs = sorted(rballs)
bballs = sorted(bballs)

for r in rballs:
  print(r)

for b in bballs:
  print(b)

