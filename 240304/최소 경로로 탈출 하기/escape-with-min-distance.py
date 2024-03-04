n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

def can_move(y, x):
    if 0 <= y < n and 0 <= x < m and arr[y][x] == '1':
        arr[y][x] = '0'
        return True
    return False

def move():
    from collections import deque
    
    q = deque([(0, 0, 0)])
    while q:
        y, x, cnt = q.popleft()
        if y == n-1 and x == m-1:
            return cnt
        
        cnt += 1
        
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_move(ny, nx):
                q.append((ny, nx, cnt))

    return -1

print(move())