n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
happy_num_cnt = 0

for i in range(n):
    cnt_num = 1
    before = arr[i][0]
    for j in range(1, n):
        now = arr[i][j]
        if now == before:
            cnt_num += 1
        elif cnt_num >= m:
            happy_num_cnt += 1
            break
        else:
            cnt_num = 1
        before = now
    else:
        if cnt_num >= m:
            happy_num_cnt += 1


for j in range(n):
    cnt_num = 1
    before = arr[0][j]
    for i in range(1, n):
        now = arr[i][j]
        if now == before:
            cnt_num += 1
        elif cnt_num >= m:
            happy_num_cnt += 1
            break
        else:
            cnt_num = 1
        before = now
    else:
        if cnt_num >= m:
            happy_num_cnt += 1

print(happy_num_cnt)