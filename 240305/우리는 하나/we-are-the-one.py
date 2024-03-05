from collections import deque

n, k, u, d = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
path, q = [], deque()
max_cnt = 0
visited = [[False] * n for _ in range(n)]
square = n*n

def can_travel(y, x, ref):
    if 0 <= y < n and 0 <= x < n and u <= abs(ref - cities[y][x]) <= d:
        return True
    return False

def travel():
    cnt = k
    new_visited = [visited[i][:] for i in range(n)]
    while q:
        y, x = q.popleft()
        ref = cities[y][x]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_travel(ny, nx, ref) and not new_visited[ny][nx]:
                new_visited[ny][nx] = True
                cnt += 1
                q.append((ny, nx))
    return cnt

def choose_cites(level, start):
    global max_cnt

    if level == k:
        q.extend(path)
        cnt = travel()
        if max_cnt < cnt:
            max_cnt = cnt
        return
    
    for i in range(start, square):
        quot, remain = divmod(i, n)
        path.append((quot, remain))
        visited[quot][remain] = True
        choose_cites(level+1, i+1)
        visited[quot][remain] = False
        path.pop()


choose_cites(0, 0)

print(max_cnt)