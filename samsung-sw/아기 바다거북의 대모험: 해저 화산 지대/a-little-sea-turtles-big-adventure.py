from collections import deque


def int_input():
    return map(int, input().split())


def in_range(pos):
    return 0 <= pos < N


def find_path(y, x):
    q = deque()
    min_dist = [[N*N] * N for _ in range(N)]
    min_dist[y][x] = 0
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if in_range(ny) and in_range(nx) and sea_info[ny][nx] == 0:
            min_dist[ny][nx] = 1
            q.append((ny, nx, ny, nx, 1))

    while q:
        y, x, n_y, n_x, dist = q.popleft()
        if y == N - 1 and x == N - 1:
            return (n_y, n_x)

        new_dist = dist + 1

        if min_dist[y][x] >= dist:
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if in_range(ny) and in_range(nx):
                    if sea_info[ny][nx] == 0 and min_dist[ny][nx] > new_dist:
                        min_dist[ny][nx] = new_dist
                        q.append((ny, nx, n_y, n_x, new_dist))

    return ()


def move(now):
    can_move = False
    for i in range(1, M + 1):
        if arrived[i] == 0:
            y, x = turtles[i]
            next_pos = find_path(y, x)
            if next_pos:
                can_move = True
                ny, nx = next_pos
                sea_info[y][x] = 0
                if ny == N - 1 and nx == N - 1:
                    arrived[i] = now
                else:
                    sea_info[ny][nx] = -i
                    turtles[i] = (ny, nx)

    return can_move


def erupt():
    for r, c, _ in volcano_arr:
        press_info[r][c] += 10

    cnt1 = cnt2 = 0

    while True:
        for i in range(K):
            r, c, P = volcano_arr[i]
            if erupted[i]:
                cnt2 += 1
            elif press_info[r][c] + heat_info[r][c] >= P:
                erupted[i] = True
                cnt2 += 1
                heat_info[r][c] = P

                q = deque()
                for j in range(4):
                    q.append((r, c, j, P))

                while q:
                    y, x, idx, val = q.popleft()
                    new_val = val // 2
                    if new_val:
                        ny, nx = y + dy[idx], x + dx[idx]
                        if in_range(ny) and in_range(nx):
                            if sea_info[ny][nx] != 1:
                                heat_info[ny][nx] += new_val
                                q.append((ny, nx, idx, new_val))

        if cnt1 == cnt2:
            break
        cnt1, cnt2 = cnt2, 0


def make_fossil():
    for i in range(1, M + 1):
        if arrived[i] == 0:
            y, x = turtles[i]
            if heat_info[y][x] >= 20:
                sea_info[y][x] = 2
                arrived[i] = -1


def initiate():
    for i in range(N):
        heat_info[i] = [0] * N

    for i in range(K):
        if erupted[i]:
            r, c, _ = volcano_arr[i]
            press_info[r][c] = 0
            erupted[i] = False


def print_arrived():
    for i in range(1, M + 1):
        if arrived[i] == 0:
            print(-1)
        else:
            print(arrived[i])


N, M, K = int_input()
sea_info = [list(int_input()) for _ in range(N)]
press_info = [[0] * N for _ in range(N)]
heat_info = [[0] * N for _ in range(N)]
erupted = [False] * K
turtles = [()]
arrived = [0] * (M + 1)
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

for num in range(1, M + 1):
    r, c = int_input()
    turtles.append((r, c))
    sea_info[r][c] = -num

volcano_arr = [list(int_input()) for _ in range(K)]

for now in range(1, 101):
    if move(now):
        erupt()
        make_fossil()
        initiate()
    else:
        break

print_arrived()
