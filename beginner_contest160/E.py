x, y, a, b, c = map(int, input().split())
p_list = sorted(list(map(int, input().split())))
q_list = sorted(list(map(int, input().split())))
r_list = sorted(list(map(int, input().split())))

p_list = p_list[a - x:]
q_list = q_list[b - y:]

pqr_list = p_list + q_list + r_list
pqr_list = sorted(pqr_list,reverse=True)
pqr_list = pqr_list[:x + y]

print(sum(pqr_list))

  