from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
limit = 10001
time_table = [[limit] * n for _ in range(n)]
rotten = deque()

for i in range(n):
    for j in range(n):
        val = grid[i][j]
        if val == 0:
            time_table[i][j] = -1
        elif val == 2:
            rotten.append((i, j, 0))
            time_table[i][j] = 0


def bfs():
    dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)

    while rotten:
        y, x, time = rotten.popleft()

        new_time = time + 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if time_table[ny][nx] > new_time and grid[ny][nx] != 2:
                    time_table[ny][nx] = new_time
                    rotten.append((ny, nx, new_time))
    

bfs()

for i in range(n):
    for j in range(n):
        if time_table[i][j] == limit:
            time_table[i][j] = -2
    print(*time_table[i])

