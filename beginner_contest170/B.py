x, y = map(int, input().split())

ans = "No"
crane = 0
while crane <= x:
  turtle = x - crane
  if 2 * crane + 4 * turtle == y:
    ans = "Yes"
  crane += 1

print(ans)