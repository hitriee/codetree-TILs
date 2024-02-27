n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
max_cnt = 0

def bomb(y, x, value):
    for i in range(1, value):
        for j in range(4):
            ny, nx = y+dy[j]*i, x+dx[j]*i
            if 0 <= ny < n and 0 <= nx < n:
                new_arr[ny][nx] = 0
    new_arr[y][x] = 0
    

def gravity(y, x, value):
    from collections import deque
    for j in range(n):
        q = deque()
        for i in range(n-1, 0, -1):
            if new_arr[i][j] == 0:
                q.append(j)
            elif q:
                bottom_i = q.popleft()
                new_arr[i][j], new_arr[bottom_i][j] = 0, new_arr[i][j]
                q.append(j)


def cnt_seq():
    num_cnt, cnt = 1, 0

    for i in range(n):
        for j in range(n-1):
            if new_arr[i][j] == new_arr[i][j+1]:
                num_cnt += 1
            else:
                if num_cnt == 2:
                    if new_arr[i][j-1] > 0:
                        cnt += 1
                num_cnt = 1

        if num_cnt == 2:
            if new_arr[-1][-1] > 0:
                cnt += 1
    
    num_cnt = 1

    for j in range(n):
        for i in range(n-1):
            if new_arr[i][j] == new_arr[i+1][j]:
                num_cnt += 1
            else:
                if num_cnt == 2:
                    if new_arr[i-1][j] > 0:
                        cnt += 1
                num_cnt = 1

        if num_cnt == 2:
            if new_arr[-1][-1] > 0:
                cnt += 1
    
    return cnt

for i in range(n):
    for j in range(n):
        new_arr = [arr[k][:] for k in range(n)]
        value = arr[i][j]

        bomb(i, j, value)
        gravity(i, j, value)
        cnt = cnt_seq()

        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)