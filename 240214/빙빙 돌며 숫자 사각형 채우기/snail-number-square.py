n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
y = x = direct_idx = 0
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
limit = n*m+1

for num in range(1, limit):
    arr[y][x] = num
    ny, nx = y + dy[direct_idx], x + dx[direct_idx]
    if not(0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0):
        direct_idx = (direct_idx+1)%4
        ny, nx = y + dy[direct_idx], x + dx[direct_idx]
    
    y, x = ny, nx

for i in range(n):
    print(*arr[i])