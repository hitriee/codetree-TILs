n = int(input())
r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split())

# Please write your code here.
dy, dx = (-2, -2, -1, -1, 1, 1, 2, 2), (-1, 1, -2, 2, -2, 2, -1, 1)

def bfs():
    from collections import deque
    
    q = deque()
    visited = [[False] * n for _ in range(n)]
    q.append((r1, c1, 0))
    visited[r1][c1] = True

    while q:
        y, x, cnt = q.popleft()
        if y == r2 and x == c2:
            return cnt
        
        new_cnt = cnt + 1
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, new_cnt))
        
    
    return -1

print(bfs())