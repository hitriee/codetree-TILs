class NumberInArr:
    def __init__(self, y, x, value):
        self.y = y
        self.x = x
        self.value = value

n, m = map(int, input().split())
position, arr, dy, dx = [NumberInArr(0, 0, 0)], [], [], []
limit = n*n+1

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        position.append(NumberInArr(i, j, arr[-1][j]))

position.sort(key=lambda number: number.value)

for i in range(-1, 2):
    for j in range(-1, 2):
        if i != 0 or j != 0:
            dy.append(i)
            dx.append(j)

for _ in range(m):
    for num in range(1, limit):
        y, x = position[num].y, position[num].x
        max_num = max_y = max_x = 0
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if max_num < arr[ny][nx]:
                    max_num = arr[ny][nx]
                    max_y, max_x = ny, nx

        position[num].y, position[num].x = max_y, max_x
        position[max_num].y, position[max_num].x = y, x
        arr[max_y][max_x], arr[y][x] = num, max_num

for i in range(n):
    print(*arr[i])