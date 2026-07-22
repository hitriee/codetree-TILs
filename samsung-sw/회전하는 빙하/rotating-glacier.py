def int_input():
    return map(int, input().split())

def in_range(y, x):
    return 0 <= y < M and 0 <= x < M

def divide_conquer(now, target, ly, lx):
    if now == target:
        half = now // 2
        for k in range(4):
            nly, nlx = ly + start_y[k] * half, lx + start_x[k] * half
            rotate(nly, nlx, half, k)
        
        return

    half = now // 2
    for k in range(4):
        nly, nlx = ly + start_y[k] * half, lx + start_x[k] * half
        divide_conquer(half, target, nly, nlx)

def rotate(s_i, s_j, length, idx):
    di, dj = dy[idx] * length, dx[idx] * length
    nj = s_j + dj
    for i in range(s_i, s_i + length):
        ni, nj = i + di, s_j + dj
        new_area[ni][nj : nj+length] = area[i][s_j : s_j+length]


def melt():
    path = []
    for y in range(M):
        for x in range(M):
            if area[y][x]:
                cnt = 0
                for k in range(4):
                    ny, nx = y+dy[k], x+dx[k]
                    if not in_range(ny, nx) or area[ny][nx] == 0:
                        cnt += 1
                if cnt >= 2:
                    path.append((y, x))

    for y, x in path:
        area[y][x] -= 1


def bfs():
    from collections import deque
    
    q = deque()
    visited = [[False] * M  for _ in range(M)]
    max_cnt = total = 0
    for i in range(M):
        for j in range(M):
            if not visited[i][j] and area[i][j]:
                cnt = 0
                visited[i][j] = True
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    total += area[y][x]
                    cnt += 1

                    for k in range(4):
                        ny, nx = y+dy[k], x+dx[k]
                        if in_range(ny, nx) and not visited[ny][nx] and area[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny, nx))

                if cnt > max_cnt:
                    max_cnt = cnt

    return f'{total}\n{max_cnt}'


N, _ = int_input()
levels = [1]
for _ in range(N):
    levels.append(levels[-1] * 2)
M = levels[-1]
area = [list(int_input()) for _ in range(levels[-1])]
queries = list(int_input())
start_y, start_x = (0, 0, 1, 1), (0, 1, 1, 0)
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

for num in queries:
    if num != 0:
        new_area = [[0] * M for _ in range(M)]
        divide_conquer(M, levels[num], 0, 0)
        area = [new_area[i][:] for i in range(M)]
    melt()

print(bfs())