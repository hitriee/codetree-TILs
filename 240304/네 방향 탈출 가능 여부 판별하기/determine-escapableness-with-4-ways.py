n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

def can_go(y, x):
    if 0 <= y < n and 0 <= x < n and arr[y][x] == '1' and not visited[y][x]:
        visited[y][x] = True
        return True
    return False

def bfs():
    from collections import deque
    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()
        if y == n-1 and x == m-1:
            return '1'
        
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_go(ny, nx):
                q.append((ny, nx))
        
    return '0'

print(bfs())