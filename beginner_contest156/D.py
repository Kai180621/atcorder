n, a, b = map(int, input().split())

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

all_pattern = 2 ** n - 1
ex_a_pattern = cmb(n,a)
ex_b_pattern = cmb(n,b)

ans = (all_pattern - ex_a_pattern - ex_b_pattern) % (10 ** 9 + 7)
print(ans)