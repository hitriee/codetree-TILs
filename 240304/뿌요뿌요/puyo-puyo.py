n = int(input())
arr = [input().split() for _ in range(n)]
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
cnt = max_size = 0


def can_bomb(y, x, ref):
    if 0 <= y < n and 0 <= x < n and arr[y][x] == ref:
        arr[y][x] = '0'
        return True
    return False

def bomb(level, y, x, ref):
    global size

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if can_bomb(ny, nx, ref):
            size += 1
            bomb(level+1, ny, nx, ref)
    

for i in range(n):
    for j in range(n):
        if arr[i][j] != '0':
            size = 0
            bomb(0, i, j, arr[i][j])
            if size >= 4:
                cnt += 1
            if max_size < size:
                max_size = size

print(cnt, max_size)