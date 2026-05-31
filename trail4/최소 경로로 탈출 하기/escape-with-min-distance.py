n, m = map(int, input().split())
a = [input().split() for _ in range(n)]

dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)

def bfs():
    from collections import deque

    q = deque()
    max_cnt = n*m
    q.append((0, 0, 0))
    visited = [[False] * m for _ in range(n) ]
    visited[0][0] = True

    while q:
        y, x, cnt = q.popleft()
        if y == n - 1 and x == m - 1:
            return cnt

        new_cnt = cnt + 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and a[ny][nx] == '1':
                    visited[ny][nx] = True
                    q.append((ny, nx, new_cnt))



    return -1


print(bfs())

