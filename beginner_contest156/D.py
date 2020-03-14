n, a, b = map(int, input().split())

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]



if a == 1 and b == 1:
  print(0)
else:
  all_pattern = pow(2, n) % (10 ** 9 + 7)
  ex_a_pattern = 
