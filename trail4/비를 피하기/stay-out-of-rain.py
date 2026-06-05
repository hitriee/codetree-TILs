from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
people = []
dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)
limit = 10001
min_duration = [[limit] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if grid[i][j] != 2:
            min_duration[i][j] = 0
        else:
            people.append((i, j, i, j, 0))

def bfs():
    dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)
    for person in people:
        q = deque([person])
        visited = [[False] * n for _ in range(n)]
        while q:
            initial_y, initial_x, y, x, time = q.popleft()
            if grid[y][x] == 3:
                min_duration[initial_y][initial_x] = time
                break
            
            new_time = time + 1
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if not visited[ny][nx] and grid[ny][nx] != 1:
                        visited[ny][nx] = True
                        q.append((initial_y, initial_x, ny, nx, new_time))
        




bfs()

for i in range(n):
    for j in range(n):
        if min_duration[i][j] == limit:
            min_duration[i][j] = -1
    print(*min_duration[i])



