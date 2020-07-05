n, k = map(int, input().split())
ps = list(map(int, input().split()))

ps = sorted(ps)

print(sum(ps[:k]))

