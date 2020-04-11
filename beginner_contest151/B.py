n, k, m = map(int, input().split())
scores = list(map(int, input().split()))

goalscore = n * m
sumscore = sum(scores)

if goalscore - sumscore > k:
  print(-1)
elif goalscore - sumscore > 0:
  print(goalscore - sumscore)
else:
  print(0)
