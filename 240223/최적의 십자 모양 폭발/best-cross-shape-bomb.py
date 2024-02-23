n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0

def bomb(y, x, value):
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(1, value):
        for j in range(4):
            ny, nx = y+dy[j]*i, x+dx[j]*i
            if 0 <= ny < n and 0 <= nx < n:
                new_arr[ny][nx] = 0
    new_arr[y][x] = 0
    

def gravity(y, x, value):
    min_x, max_x = max(x-value+1, 0), min(x+value, n)
    min_y, max_y = max(y-value+1, 0), min(y+value, n)

    for j in range(min_x, max_x):
        if j != x:
            for i in range(y-1, -1, -1):
                new_arr[i][j], new_arr[i+1][j] = new_arr[i+1][j], new_arr[i][j]

    while max_y < n:
        new_arr[min_y][x], new_arr[max_y][x] = new_arr[max_y][x], new_arr[min_y][x]
        max_y += 1
        min_y += 1
 

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