import itertools

n = int(input())
ps = tuple(map(int, input().split()))
qs = tuple(map(int, input().split()))

nli = [i for i in range(1, n+1)]
# print(nli)

anss = list(itertools.permutations(nli, n))
# print(anss)

ans = abs(anss.index(ps) - anss.index(qs))
print(ans)