n, m = map(int, input().split())
rectangle = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
y = x = idx = 0

for num in range(1, n*m+1):
    rectangle[y][x] = num
    ny, nx = y+dy[idx], x+dx[idx]
    if 0 <= ny < n and 0 <= nx < m and rectangle[ny][nx] == 0:
        y, x = ny, nx
    else:
        idx = (idx+1) % 4
        y, x = y+dy[idx], x+dx[idx]

for i in range(n):
    print(*rectangle[i])