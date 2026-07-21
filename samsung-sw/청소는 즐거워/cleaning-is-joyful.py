def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def find_delta():
    arr = []
    for i in range(4):
        j1, j2 = (i-1)%4, (i+1)%4
        dr, dc = [], []
        
        for multiple in (-1, 0, 1):
            for j in (j1, j2):
                dr.append(multiple*dy[i]+dy[j])
                dc.append(multiple*dx[i]+dx[j])
        
        
        for j in (j1, j2):
            dr.append(2*dy[j])
            dc.append(2*dx[j])
        
        dr.append(2*dy[i])
        dc.append(2*dx[i])
        

        arr.append([tuple(dr), tuple(dc)])

    return arr

def move(r, c, idx):
    initial = remain = dust[r][c]
    total = dust[r][c] = 0
    dr, dc = delta[idx]

    for i in range(9):
        nr, nc = r+dr[i], c+dc[i]
        val = int(initial * ratio[i//2])
        remain -= val
        if in_range(nr, nc):
            dust[nr][nc] += val
        else:
            total += val
    
    nr, nc = r+dy[idx], c+dx[idx]
    if in_range(nr, nc):
        dust[nr][nc] += remain
    else:
        total += remain

    return total

def sweep():
    y = x = N//2
    total = idx = 0
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True

    while True:
        ny, nx = y+dy[idx], x+dx[idx]
        if not in_range(ny, nx):
            return total
        
        if visited[ny][nx]:
            idx = (idx-1) % 4
        else:
            visited[ny][nx] = True
            total += move(ny, nx, idx)
            idx = (idx+1) % 4
            y, x = ny, nx


N = int(input())
dust = [list(map(int, input().split())) for _ in range(N)]
dy, dx = (0, 1, 0, -1), (-1, 0, 1, 0)
ratio = [0.01, 0.07, 0.1, 0.02, 0.05]
delta = find_delta()

print(sweep())