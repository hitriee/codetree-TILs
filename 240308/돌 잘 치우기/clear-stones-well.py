from collections import deque

n, k, m = map(int, input().split())
arr = [input().split() for _ in range(n)]
start_points = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(k)]
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[False] * n for _ in range(n)]
rocks = []
max_cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            rocks.append((i, j))

rock_cnt = len(rocks)
cnt_limit = n*n - rock_cnt + m

for r, c in start_points:
    visited[r][c] = True

def move():
    cnt = k
    q = deque(start_points)
    new_visited = [visited[i][:] for i in range(n)]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == '0' and not new_visited[nr][nc]:
                new_visited[nr][nc] = True
                cnt += 1
                q.append((nr, nc))

    return cnt

def choose_rocks(level, start):
    global max_cnt
    
    if max_cnt == cnt_limit:
        return

    if level == m:
        cnt = move()
        # print(cnt)
        if max_cnt < cnt:
            max_cnt = cnt
        return

    for i in range(start, rock_cnt):
        r, c = rocks[i]

        arr[r][c] = '0'
        choose_rocks(level+1, i+1)
        arr[r][c] = '1'

choose_rocks(0, 0)

print(max_cnt)