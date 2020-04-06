a1, a2, a3 = map(int, input().split())
n = a1 + a2 + a3

ans = 0 

def dfs(x, y, z, count):
  global ans
  if x > a1 or y > a2 or z > a3: return
  if x < y or y < z: return
  if count == n:
    ans += 1
    return
  
  dfs(x + 1, y, z, count + 1)
  dfs(x, y + 1, z, count + 1)
  dfs(x, y, z + 1, count + 1)

dfs(0, 0, 0, 0)
print(ans)
