n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
happy_num_cnt = 0

for i in range(n):
    cnt_num = [0] * 101
    for j in range(m):
        cnt_num[arr[i][j]] += 1
    for k in range(1, 101):
        if cnt_num[k] >= m:
            happy_num_cnt += 1
            break

for j in range(n):
    cnt_num = [0] * 101
    for i in range(n):
        cnt_num[arr[i][j]] += 1
    for k in range(1, 101):
        if cnt_num[k] >= m:
            happy_num_cnt += 1
            break

print(happy_num_cnt)