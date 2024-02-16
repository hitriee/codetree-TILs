N = int(input())
arr = [input().split() for _ in range(N)]
max_cnt = 0
for start_i in range(N-2):
    for start_j in range(N-2):
        cnt = 0
        for di in range(3):
            i = start_i+di
            for dj in range(3):
                if arr[i][start_j+dj] == '1':
                    cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)