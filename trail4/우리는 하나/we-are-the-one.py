from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
limit, max_cnt = n*n, 0
path = []

def dfs(level, start):
    global max_cnt

    if level == k:
        cnt = bfs()
        if max_cnt < cnt:
            max_cnt = cnt
        return
    
    for i in range(start, limit):
        y, x = i // n, i % n
        visited[y][x] = True
        path.append((y, x))
        dfs(level+1, i+1)
        visited[y][x] = False
        path.pop()
    

def bfs():
    cnt = 0
    q = deque(path)
    arr = []
    
    while q:
        y, x = q.popleft()
        cnt += 1
        height = grid[y][x]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and u <= abs(grid[ny][nx] - height) <= d:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    arr.append((ny, nx))
    
    for y, x in arr:
        visited[y][x] = False

    return cnt

dfs(0, 0)

print(max_cnt)
        