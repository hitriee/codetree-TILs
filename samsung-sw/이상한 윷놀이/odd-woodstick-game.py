def minus_one(num):
    return int(num) - 1


def int_input(func=int):
    return map(func, input().split())


def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


def ended_turn():
    for i in range(1, 1001):
        for j in range(K):
            y, x, idx, d = items[j]
            ny, nx, nd = y + dy[d], x + dx[d], d
            for _ in range(2):
                if not in_range(ny, nx) or board[ny][nx] == 2:
                    nd = nd ^ 1
                    ny, nx = y + dy[nd], x + dx[nd]
                else:
                    break
            else:
                items[j][-1] = nd ^ 1
                continue

            state = state_arr[y][x]
            length = len(state)
            new_length = len(state_arr[ny][nx])

            if board[ny][nx] == 1:
                for k in range(length - 1, idx, -1):
                    items[state[k]][:-1] = [ny, nx, new_length + length - k - 1]
                    state_arr[ny][nx].append(state[k])
                items[state[idx]] = [ny, nx, new_length + length - idx - 1, nd]
                state_arr[ny][nx].append(state[idx])

            else:
                items[state[idx]] = [ny, nx, new_length, nd]
                state_arr[ny][nx].append(state[idx])
                for k in range(idx + 1, length):
                    items[state[k]][:-1] = [ny, nx, new_length + k - idx]
                    state_arr[ny][nx].append(state[k])

            state_arr[y][x] = state[:idx]

            if len(state_arr[ny][nx]) >= 4:
                return i

    return -1


N, K = int_input()
board = [list(int_input()) for _ in range(N)]
state_arr = [[[] for _ in range(N)] for _ in range(N)]
dy, dx = (0, 0, -1, 1), (1, -1, 0, 0)
items = []

for i in range(K):
    y, x, d = int_input(minus_one)
    items.append([y, x, 0, d])
    state_arr[y][x].append(i)

print(ended_turn())
