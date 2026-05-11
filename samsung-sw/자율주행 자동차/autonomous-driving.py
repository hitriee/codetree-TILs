n, m = map(int, input().split())
y, x, d = map(int, input().split())
road = [input().split() for _ in range(n)]
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
visited = [[False] * m for _ in range(n)]
visited[y][x] = True
cnt = 1

while True:
    nd = (d-1) % 4
    for _ in range(4):
        nx, ny = x+dx[nd], y+dy[nd]
        if road[ny][nx] == '0' and not visited[ny][nx]:
            x, y, d = nx, ny, nd
            visited[ny][nx] = True
            cnt += 1
            break
        nd = (nd-1) % 4
    else:
        nd = (d-2) % 4
        nx, ny = x+dx[nd], y+dy[nd]
        if road[ny][nx] == '1':
            break
        x, y = nx, ny

print(cnt)