MOD = 998244353

fact = [0] * 220000
invfact = [0] * 220000

n, m, k = map(int, input().split())

ans = 0
def nCk(n, k):
  return fact

for i in range(0, k + 1):
  ans += (m * pow(m - 1, n - k - 1, MOD) * nCk(n - 1, k)) % MOD
  
prin(ans % MOD)