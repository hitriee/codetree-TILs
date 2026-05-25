n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]
max_total = [0] * n
max_total[0] = p[0]

# Please write your code here.
for i in range(1, n):
    start, val = s[i], p[i]
    max_val = val
    for j in range(i):
        end = e[j]
        if end < start:
            max_val = max(max_total[j] + val, max_val)
    max_total[i] = max_val
    

print(max(max_total))
