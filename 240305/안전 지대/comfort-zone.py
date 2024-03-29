from sys import setrecursionlimit

setrecursionlimit(5000)

N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
max_safe_cnt = limit = 0

def possible(y, x, ref):
    if 0 <= y < N and 0 <= x < M and not visited[y][x]:
        visited[y][x] = True
        if town[y][x] > k:
            return True
    return False

def cnt_safe_area(y, x, ref):
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if possible(ny, nx, ref):
            cnt_safe_area(ny, nx, ref)

for i in range(N):
    for j in range(M):
        if town[i][j] > limit:
            limit = town[i][j]

height = limit

for k in range(1, limit):
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = True
                if town[i][j] > k:
                    cnt += 1 
                    cnt_safe_area(i, j, k)

    if max_safe_cnt < cnt:
        max_safe_cnt = cnt
        height = k

print(height, max_safe_cnt)