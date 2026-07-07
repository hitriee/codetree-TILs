def int_input(func=int):
    return map(func, input().split())


def minus_one(num):
    return int(num) - 1

def search():
    for i in range(N):
        if board[i][j]:
            idx = board[i][j][0]
            board[i][j] = []
            return idx
    return -1


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def find_new_pos(y, x, d):
    while not in_range(y, x):
        if d == 0:
            y = -y
        elif d == 1:
            y = N - (y - N) - 2
        elif d == 2:
            x = M - (x - M) - 2
        else:
            x = -x
        d ^= 1
    return (y, x, d)


def move(idx, limit):
    new_info = []
    for i in range(limit):
        if i != idx:
            y, x, s, d, b = info[i]
            board[y][x] = []
            ny, nx = y + s * dy[d], x + s * dx[d]
            # if in_range(ny, nx):
            #     y, x = ny, nx
            # else:
            y, x, d = find_new_pos(ny, nx, d)

            new_info.append((y, x, s, d, b))

    return new_info


def eat():
    removed = [False] * k
    over_two = set()
    new_info = []

    for idx in range(k):
        y, x = info[idx][:2]
        if board[y][x]:
            over_two.add((y, x))
        board[y][x].append(idx)

    if not over_two:
        return info

    for y, x in over_two:
        board[y][x].sort(key=lambda idx: -info[idx][-1])
        length = len(board[y][x]) - 1
        for _ in range(length):
            removed[board[y][x].pop()] = True

    idx = 0
    for i in range(k):
        if not removed[i]:
            y, x = info[i][:2]
            new_info.append(tuple(info[i]))
            board[y][x] = [idx]
            idx += 1

    return new_info


N, M, k = int_input()
board = [[[] for _ in range(M)] for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
info = []
converted_pos = [0, N - 1, 0, M - 1]
for i in range(k):
    y, x, s, d, b = int_input(minus_one)
    info.append((y, x, s + 1, d, b + 1))
    board[y][x].append(i)
total_size = 0

for j in range(M):
    idx = search()
    limit = k
    if idx != -1:
        total_size += info[idx][-1]
        k -= 1

    info = move(idx, limit)
    
    info = eat()
    k = len(info)

# 채취한 곰팡이 크기의 총 합
print(total_size)

