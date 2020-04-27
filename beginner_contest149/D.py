n, k = map(int, input().split())
r, s, p = map(int, input().split())
ts = input()
hands = []

ans = 0
for i, t in enumerate(ts):
  if t == "r":
    if not i - k < 0:
      if hands[i - k] == "p":
        ans += 0
        hands.append(t)
        continue
    ans += p
    hands.append("p")
  elif t == "s":
    if not i - k < 0:
      if hands[i - k] == "r":
        ans += 0
        hands.append(t)
        continue
    ans += r
    hands.append("r")
  elif t == "p":
    if not i - k < 0:
      if hands[i - k] == "s":
        ans += 0
        hands.append(t)
        continue
    ans += s
    hands.append("s")

print(ans)
