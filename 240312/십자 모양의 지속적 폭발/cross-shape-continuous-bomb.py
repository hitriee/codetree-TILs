n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
selected_row = [0] * n
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
def gravity(y, x):
    temp = []
    for i in range(y, -1, -1):
        if arr[i][x]:
            temp.append(arr[i][x])
    length = len(temp)
    for i in range(length):
        arr[y-i][x] = temp[i]
    
    for i in range(y-length, -1, -1):
        arr[i][x] = 0


for _ in range(m):
    col = int(input())-1
    row = selected_row[col]
    while row < n:
        num = arr[row][col]
        if num:
            break
        row += 1
    else:
        continue
    
    arr[row][col] = 0
    selected_row[col] += 1

    path = []
    for i in range(4):
        ny, nx = row, col
        for _ in range(1, num):
            ny += dy[i]
            nx += dx[i]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx]:
                arr[ny][nx] = 0
                path.append((ny, nx))

    for y, x in path:
        if x != col:
            gravity(y, x)

for i in range(n):
    print(*arr[i])