n, m = map(int, input().split())
alp_to_num, num_to_alp = {}, [''] * (n+1)

for i in range(1, n+1):
    alp = input()
    alp_to_num[alp] = i
    num_to_alp[i] = alp

for _ in range(m):
    key = input()
    if key.isdigit():
        print(num_to_alp[int(key)])
    else:
        print(alp_to_num[key])