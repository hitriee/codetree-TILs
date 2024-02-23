n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

cnt = [[0] * n for _ in range(n)]
for _ in range(m):
    y, x = tuple(map(lambda x: int(x)-1, input().split()))
    cnt[y][x] += 1

for _ in range(t):
    new_cnt = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if cnt[y][x] == 1:
                max_num = max_y = max_x = 0
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if 0 <= ny < n and 0 <= nx < n and max_num < arr[ny][nx]:
                        max_num = arr[ny][nx]
                        max_y, max_x = ny, nx
                new_cnt[max_y][max_x] += 1

    for y in range(n):
        for x in range(n):
            value = new_cnt[y][x]
            if value >= 2:
                m -= value
                value = 0
            cnt[y][x] = value

print(m)