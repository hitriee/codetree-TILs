n, m = map(int, input().split())
alp = [chr(ord('A') + i) for i in range(26)]
arr = [[''] * m for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
y = x = alp_i = d_i = 0

for _ in range(n*m):
    arr[y][x] = alp[alp_i]
    ny, nx = y+dy[d_i], x+dx[d_i]
    
    if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == '':
        y, x = ny, nx
    else:
        d_i = (d_i + 1) % 4
        y, x = y+dy[d_i], x+dx[d_i]
    
    alp_i = (alp_i + 1) % 26

for i in range(n):
    print(' '.join(arr[i]))