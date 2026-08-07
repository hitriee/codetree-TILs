from heapq import heappush, heappop


def minus_one(num):
    return int(num) - 1


def minus_one_input():
    return map(minus_one, input().split())


def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


def calc_duration(r1, c1, r2, c2):
    heap = []
    min_duration = [[[max_duration] * 6 for _ in range(N)] for _ in range(N)]
    heap.append((0, 1, r1, c1))
    min_duration[r1][c1][1] = 0

    while heap:
        # print(heap)
        duration, jump, y, x = heappop(heap)
        if y == r2 and x == c2:
            return duration

        if duration <= min_duration[y][x][jump]:
            limit = min(jump + 2, 6)
            # 점프력 변경
            for j in range(1, limit):
                new_duration = duration
                if j > jump:
                    new_duration += j * j
                elif j < jump:
                    new_duration += 1

                if new_duration < min_duration[y][x][j]:
                    heappush(heap, (new_duration, j, y, x))
                    min_duration[y][x][j] = new_duration

            # 점프력 변경 & 점프
            for i in range(4):
                delta_y, delta_x = dy[i], dx[i]
                ny, nx = y, x
                for j in range(1, limit):
                    ny += delta_y
                    nx += delta_x

                    if not in_range(ny, nx):
                        break

                    val = pond[ny][nx]

                    if val == '#':
                        break

                    if val == '.':
                        new_duration = duration + 1

                        if j < jump:
                            new_duration += 1
                        elif j > jump:
                            new_duration += j*j

                        if min_duration[ny][nx][j] > new_duration:
                            heappush(heap, (new_duration, j, ny, nx))
                            min_duration[ny][nx][j] = new_duration
                # else:
                #     for j in range(jump+2, 6):
                #



    return -1


N = int(input())
pond = [input() for _ in range(N)]
Q = int(input())
dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)
max_duration = int(1e9)
for _ in range(Q):
    print(calc_duration(*minus_one_input()))