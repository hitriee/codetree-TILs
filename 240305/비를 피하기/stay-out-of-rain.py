n, h, m = map(int, input().split())
arr = [input().split() for _ in range(n)]
new_arr = [['0']*n for _ in range(n)]
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

def can_move(y, x):
    if 0 <= y < n and 0 <= x < n and arr[y][x] != '1':
        return True
    return False

def move_to_safe_area(i, j):
    from collections import deque
    q = deque()
    q.append((i, j, 0))
    visited = [[False] * n for _ in range(n)]
    
    while q:
        y, x, time = q.popleft()
        if arr[y][x] == '3':
            return str(time)
        
        time += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_move(ny, nx) and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, time))

    return '-1'



for i in range(n):
    for j in range(n):
        if arr[i][j] == '2':
            new_arr[i][j] = move_to_safe_area(i, j)
    print(' '.join(new_arr[i]))