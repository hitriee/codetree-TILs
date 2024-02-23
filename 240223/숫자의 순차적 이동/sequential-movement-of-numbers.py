n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [], []
limit = n*n+1
position = [() for _ in range(limit)]

for i in range(-1, 2):
    for j in range(-1, 2):
        if i != 0 or j != 0:
            dy.append(i)
            dx.append(j)

for y in range(n):
    for x in range(n):
        position[arr[y][x]] = (y, x)


for _ in range(m):
    for num in range(1, limit):
        y, x = position[num]
        max_num = max_y = max_x = 0
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if max_num < arr[ny][nx]:
                    max_num = arr[ny][nx]
                    max_y, max_x = ny, nx

        arr[max_y][max_x], arr[y][x] = num, max_num
        position[num], position[max_num] = (max_y, max_x), (y, x)


for i in range(n):
    print(*arr[i])