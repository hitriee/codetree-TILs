n = int(input())
r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split())
visited = [[False] * n for _ in range(n)]
dy, dx = [], []

for i in range(1, 3):
    for j in (-1, 1):
        for _ in range(2):
            dy.append(i*j)
        dx.append(3-abs(i))
        dx.append(abs(i)-3)

def can_move(y, x):
    if 0 <= y < n and 0 <= x < n and not visited[y][x]:
        visited[y][x] = True
        return True
    return False

def move_knight():
    from collections import deque

    q = deque()
    q.append((r1, c1, 0))
    while q:
        y, x, cnt = q.popleft()
        if y == r2 and x == c2:
            return cnt
        
        cnt += 1
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if can_move(ny, nx):
                q.append((ny, nx, cnt))

    return -1


print(move_knight())