n, k = map(int, input().split())
arr = [input().split() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
minus_one = lambda x: int(x) - 1
cnt = 0

def can_go(y, x):
    if 0 <= y < n and 0 <= x < n and arr[y][x] == '0' and not visited[y][x]:
        visited[y][x] = True
        return True
    
    return False

def travel(*initial):
    from collections import deque
    q = deque()
    q.append(initial)
    each_cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_go(ny, nx):
                each_cnt += 1
                q.append((ny, nx))

    return each_cnt


for _ in range(k):
    r, c = map(minus_one, input().split())
    if not visited[r][c]:
        visited[r][c] = True
        cnt += 1
    cnt += travel(r, c)

print(cnt)