n = int(input())
y = x = n-1
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
idx = 0
arr = [[0] * n for _ in range(n)]

for num in range(n*n, 0, -1):
    arr[y][x] = num
    ny, nx = y + dy[idx], x + dx[idx]
    if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:
        y, x = ny, nx
    else:
        idx = (idx + 1) % 4
        y, x = y + dy[idx], x + dx[idx]
    
for i in range(n):
    print(*arr[i])