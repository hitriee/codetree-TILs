from collections import deque


def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


def rotate():
    middle = list(board[half])
    for i in range(N):
        board[half][i] = board[i][half]

    for j in range(N):
        board[j][half] = middle[N - 1 - j]

    for s_i, e_i in start_end:
        for s_j, e_j in start_end:
            new_square = list(zip(*[board[i][s_j:e_j] for i in range(e_i - 1, s_i - 1, -1)]))
            for i in range(s_i, e_i):
                board[i][s_j:e_j] = list(new_square[i - s_i])


def bfs(i, j, target, num, group_num):
    q = deque()
    cnt = 1
    q.append((i, j))

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if in_range(ny, nx):
                if board[ny][nx] == target and group_num[ny][nx] == 0:
                    group_num[ny][nx] = num
                    q.append((ny, nx))
                    cnt += 1

    return cnt


def make_group():
    group_info = []
    group_num = [[0] * N for _ in range(N)]
    num = 1

    for i in range(N):
        for j in range(N):
            if group_num[i][j] == 0:
                key = board[i][j]
                group_num[i][j] = num
                cnt = bfs(i, j, key, num, group_num)
                group_info.append((i, j, key, num, cnt))
                num += 1

    return group_info, group_num


def calc_score():
    group_info, group_num = make_group()
    visited = [[False] * N for _ in range(N)]
    score = 0

    for i, j, color, num, cnt in group_info:
        visited[i][j] = True
        around = {}
        q = deque()
        q.append((i, j))
        while q:
            y, x = q.popleft()

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if in_range(ny, nx):
                    new_num = group_num[ny][nx]
                    if new_num != num:
                        around[new_num] = around.get(new_num, 0) + 1
                    elif not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))

        for key in around:
            if key > num:
                _, _, new_color, _, new_cnt = group_info[key - 1]
                result = (cnt + new_cnt) * color * new_color * around[key]
                score += result

    return score


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dy, dx = (0, 1, 0, -1), (-1, 0, 1, 0)
half = N // 2
start_end = [(0, half), (half + 1, N)]
total = calc_score()

for _ in range(3):
    rotate()
    total += calc_score()

print(total)