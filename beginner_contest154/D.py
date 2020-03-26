n, k = map(int, input().split())
p_list = list(map(int, input().split()))

i = 0

expect_list = []
# 全部の期待値を求めた
for p in p_list:
  expect_list.append((p + 1) / 2)

# print(expect_list)

# 累積値を求めよう
accum_list = []
i = 0
while i < n:
  accum_list.append(sum(expect_list[0:i+1]))
  i += 1

# print(accum_list)

i = k - 1
max = 0
while i < n:
  dif = accum_list[i] - accum_list[i - k]
  if max < dif:
    max = dif
  i += 1

print(max)

