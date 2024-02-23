N = int(input())
y, x = map(lambda x: int(x)-1, input().split())
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
arr = [input() for _ in range(N)]
time, i, initial_y, initial_x = 1, 0, y, x

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

while True:
    ny, nx = y+dy[i], x+dx[i]
    if not in_range(ny, nx):
        break
    if arr[ny][nx] == '#':
        i = (i+1)%4
    else:
        time += 1
        y, x = ny, nx
        ni = (i-1)%4
        ny += dy[ni]
        nx += dx[ni]
        if arr[ny][nx] != '#':
            y, x, i = ny, nx, ni
            time += 1
            
    
    if initial_y == y and initial_x == x and i == 0:
        time = -1
        break

print(time)