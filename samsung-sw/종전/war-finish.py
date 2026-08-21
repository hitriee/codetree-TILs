from collections import deque

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def make_rectangle(y, x, h, w):
    edges = [(y, x)]
    len_arr = (h, w, h)
    ny, nx = y, x

    for i in range(3):
        ny += dy_r[i] * len_arr[i]
        nx += dx_r[i] * len_arr[i]
        if in_range(ny, nx):
            edges.append((ny, nx))
        else:
            return []
    return edges

def split_area(start_arr, area):
    cnt_arr = [0] * 5
    for i in range(5):
        q = deque(start_arr[i])
        cnt = 0
        while q:
            y, x = q.popleft()

            for j in range(4):
                ny, nx = y+dy_a[j], x+dx_a[j]
                if in_range(ny, nx) and area[ny][nx] == -1:
                    area[ny][nx] = i
                    q.append((ny, nx))
        
        cnt_arr[i] = cnt
    
    for i in range(N):
        for j in range(N):
            cnt_arr[area[i][j]] += arr[i][j]
    
    return max(cnt_arr) - min(cnt_arr)


def calc_dif(len_arr, edges):
    area = [[-1] * N for _ in range(N)]
    start_arr = [[] for _ in range(5)]

    for i in range(4):
        y, x = edges[i]
        j = (i+1) % 4
        
        ny, nx = y, x
        while in_range(ny, nx):
            area[ny][nx] = i
            r, c = ny + dy_a[j], nx + dx_a[j]
            if in_range(r, c):
                start_arr[i].append((r, c))
                area[r][c] = i
            
            ny += dy_a[i]
            nx += dx_a[i]
        
        area[y][x] = 4
        start_arr[-1].append((y, x))
        
        for _ in range(len_arr[i%2]):
            y += dy_r[i]
            x += dx_r[i]
            area[y][x] = 4
            start_arr[-1].append((y, x))
    
    return split_area(start_arr, area)
        
    

def find_min_dif():
    min_dif = 40000
    for i in range(2, N):
        for j in range(1, N):
            # i, j = 2, 1
            for h in range(1, N):
                for w in range(1, N):
                    edges = make_rectangle(i, j, h, w)
                    if edges:
                        dif = calc_dif([h-1, w-1], edges)
                        if dif < min_dif:
                            min_dif = dif
                    else:
                        break
    
    return min_dif

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy_r, dx_r = (-1, -1, 1, 1), (1, -1, -1, 1)
dy_a, dx_a = (1, 0, -1, 0), (0, 1, 0, -1)


print(find_min_dif())