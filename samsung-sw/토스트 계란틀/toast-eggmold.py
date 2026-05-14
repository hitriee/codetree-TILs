from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
cnt = 0


def bfs(*initial):

    q.append(initial)
    path = [initial]

    while q:
        y, x = q.popleft()
        for idx in range(4):
            ny, nx = y+dy[idx], x+dx[idx]
            if 0 <= ny < N and 0 <= nx < N:

                if not visited[ny][nx] and L <= abs(arr[y][x] - arr[ny][nx]) <= R:
                    visited[ny][nx] = True
                    path.append((ny, nx))
                    q.append((ny, nx))


    length = len(path)
    if length > 1:
        total = sum([arr[y][x] for y, x in path])
        new_val = total // length

        for y, x in path:
            arr[y][x] = new_val

        return True
    return False


while True:
    need_break = True
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                if bfs(i, j):
                    need_break = False

    if need_break:
        break

    cnt += 1

print(cnt)