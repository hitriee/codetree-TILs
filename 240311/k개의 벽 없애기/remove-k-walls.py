n, k = map(int, input().split())
arr = [input().split() for _ in range(n)]
r1, c1 = map(lambda x: int(x)-1, input().split())
r2, c2 = map(lambda x: int(x)-1, input().split())
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

def can_move(y, x):
    if 0 <= y < n and 0 <= x < n:
        return True
    return False

def remove_walls():
    from collections import deque
    q = deque()
    visited = [[k+1] * n for _ in range(n)]
    q.append((r1, c1, 0, 0))
    
    while q:
        y, x, cnt, time = q.popleft()
        if cnt > k:
            continue
        if y == r2 and x == c2:
            return time
        time += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_move(ny, nx):
                if arr[ny][nx] == '0':
                    if visited[ny][nx] > cnt:
                        visited[ny][nx] = cnt
                        q.append((ny, nx, cnt, time))
                elif visited[ny][nx] > cnt+1:
                    visited[ny][nx] = cnt+1
                    q.append((ny, nx, cnt+1, time))

    return -1

print(remove_walls())