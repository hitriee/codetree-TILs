def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
    visited = [[0] * M for _ in range(N)]
    one = []

    for i in range(N):
        for j in range(M):
            val = arr[i][j]
            if val == 6:
                visited[i][j] = 1
            if 0 < val < 6:
                visited[i][j] = 1
                one.append((i, j, val))

    K, max_cnt = len(one), 0

    def find_direction(idx):
        if idx == 1:
            return lambda x: (x,)
        elif idx == 2:
            return lambda x: (x, (x + 2) % 4)
        elif idx == 3:
            return lambda x: (x, (x + 1) % 4)
        elif idx == 4:
            return lambda x: (x, (x + 1) % 4, (x - 1) % 4)

        return lambda x: tuple(range(0, 4))

    def dfs(level):
        nonlocal max_cnt

        if level == K:
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if visited[i][j] != 0:
                        cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt
            return

        y, x, val = one[level]

        directions = set()
        for i in range(4):
            directions.add(find_direction(val)(i))

        for each in directions:
            path = []
            for d in each:
                ny, nx = y + dy[d], x + dx[d]
                while 0 <= ny < N and 0 <= nx < M and arr[ny][nx] != 6:
                    path.append((ny, nx))
                    visited[ny][nx] += 1
                    ny += dy[d]
                    nx += dx[d]

            dfs(level + 1)
            for ny, nx in path:
                visited[ny][nx] -= 1

    dfs(0)

    return N * M - max_cnt


print(main())