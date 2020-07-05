t = int(input())

for _ in range(t):
  n, a, b, c, d = map(int, input().split())
  dp = {}

  def calc(x):
    global dp
    i = -4
    while i <= 4:
      if x + i < 0:
        continue
      if dp[x + i]:
        dp[x + i] = max(dp[x] + i * d, dp[x + i])
      else:
        dp[x + i] = dp[x] + i * d
      if (x + i) % 2 == 0:
        if dp[(x + i) % 2]:
          dp[(x + i) // 2] = max(dp[x + i] + a, dp[(x + i) // 2])
        else:
          dp[x + i] = dp[x + i] + a
      if (x + i) % 3 == 0:
        if dp[(x + i) // 3]:
          dp[(x + i) // 2] = max(dp[x + i] + b, dp[(x + i) // 3])
        else:
          dp[x + i] = dp[x + i] + b
      if (x + i) % 5 == 0:
        if dp[(x + i) // 5]:
          dp[(x + i) % 5] = max(dp[x + i] + c, dp[(x + i) // 5])
        else:
          dp[x + i] = dp[x + i] + c
          

  dp[n] = 0
  while n != 1:







  


  
  
