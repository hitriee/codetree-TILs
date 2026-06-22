from collections import deque


def minus_one(num):
    return int(num) - 1


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def move_around(y, x, idx):
    while True:
        for j in (idx, (idx + 1) % 4, (idx - 1) % 4, (idx + 2) % 4):
            ny, nx = y + dy[j], x + dx[j]
            if in_range(ny, nx) and not visited[ny][nx]:
                if sea_info[ny][nx] == '0':
                    visited[ny][nx] = True
                    y, x, idx = ny, nx, j
                    path.append(f'{ny + 1} {nx + 1}')
                    break
        else:
            return (y, x, idx)


def choose(*args):
    q = deque()
    q.append((*args, 0))
    revisited = [[False] * n for _ in range(n)]
    min_dist = n * n
    candidate = []

    while q:
        y, x, dist = q.popleft()
        new_dist = dist + 1
        for j in (3, 0, 1, 2):
            ny, nx = y + dy[j], x + dx[j]
            if in_range(ny, nx) and sea_info[ny][nx] == '0':
                if not revisited[ny][nx]:
                    if visited[ny][nx]:
                        revisited[ny][nx] = True
                        q.append((ny, nx, new_dist))
                    elif min_dist >= new_dist:
                        revisited[ny][nx] = True
                        min_dist = new_dist
                        candidate.append((ny, nx))
                    else:
                        break
    if not candidate:
        return args

    candidate.sort()
    return candidate[0]



def go_to_ocean(y, x, idx):
    revisited = [[False] * n for _ in range(n)]
    final_y, final_x = choose(y, x)

    if final_y == y and final_x == x:
        return ()

    visited[final_y][final_x] = True
    path.append(f'{final_y + 1} {final_x + 1}')

    q = deque()
    q.append((y, x, idx))

    while q:
        r, c, d = q.popleft()
        if final_y == r and final_x == c:
            return (r, c, d)

        for j in (3, 0, 1, 2):
            nr, nc = r + dy[j], c + dx[j]
            if in_range(nr, nc) and sea_info[nr][nc] == '0':
                if visited[nr][nc] and not revisited[nr][nc]:
                    revisited[nr][nc] = True
                    q.append((nr, nc, j))


n, r, c, d = map(minus_one, input().split())
n += 1
sea_info = [input().split() for _ in range(n)]
path = [f'{r + 1} {c + 1}']
dy, dx = (1, 0, -1, 0), (0, 1, 0, -1)
d_to_idx = (2, 0, 3, 1)
d = d_to_idx[d]
visited = [[0] * n for _ in range(n)]
visited[r][c] = True

while True:
    r, c, d = move_around(r, c, d)
    result = go_to_ocean(r, c, d)
    if not result:
        break
    r, c, d = result

for position in path:
    print(position)

