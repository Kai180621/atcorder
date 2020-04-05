n, k = map(int, input().split())

rem = n % k
rem_minus = (rem - k) * - 1

if rem >= rem_minus:
  print(rem_minus)
else:
  print(rem)