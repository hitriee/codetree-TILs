n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
happy_num_cnt = 0

for i in range(n):
    cnt_num = 1
    for j in range(1, n):
        if arr[i][j] == arr[i][j-1]:
            cnt_num += 1
        elif cnt_num < m:
            cnt_num = 1
        else:
            happy_num_cnt += 1
            break
    else:
        if cnt_num >= m:
            happy_num_cnt += 1


for j in range(n):
    cnt_num = 1
    for i in range(1, n):
        if arr[i][j] == arr[i-1][j]:
            cnt_num += 1
        elif cnt_num < m:
            cnt_num = 1
        else:
            happy_num_cnt += 1
            break
    else:
        if cnt_num >= m:
            happy_num_cnt += 1

print(happy_num_cnt)