from collections import deque

def dfs(level, start):
    global max_cnt

    if level == m:
        cnt = bfs()
        if cnt > max_cnt:
            max_cnt = cnt
        return
    
    for i in range(start, l):
        y, x = rocks[i]
        grid[y][x] = 0
        dfs(level+1, i+1)
        grid[y][x] = 1


def bfs():
    cnt = 0
    q = deque(points)
    arr = []

    while q:
        y, x = q.popleft()
        cnt += 1

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and grid[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    arr.append((ny, nx))

    
    for y, x in arr:
        visited[y][x] = False
    
    return cnt






n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0
rocks, points = [], []
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
visited = [[False] * n for _ in range(n)]
for _ in range(k):
    y, x = map(lambda x: int(x) - 1, input().split())
    visited[y][x] = True
    points.append((y, x))

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            rocks.append((i, j))

l = len(rocks)
dfs(0, 0)
print(max_cnt)
        

