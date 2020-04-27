s = input()
l = len(s)

ans = 0

dps = [0] * l
mods = [0] * l
s = s[::-1]

dps.append(int(s[0]))

i = 1
while i < l:
  dps[i] = int(10 * s[i] + s[i - 1])
  mods[i] = dps[i] % 2019
  i += 1

print(dps, mods)



  