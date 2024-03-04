n, k = map(int, input().split())
arr = [input().split() for _ in range(n)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
new_arr = [['-1'] * n for _ in range(n)]

def can_spread(y, x, cnt):
    if 0 <= y < n and 0 <= x < n and new_arr[y][x] == '-2':
        new_arr[y][x] = str(cnt)
        return True
    return False

def spread():
    from collections import deque

    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                new_arr[i][j] = '0'
                q.append((i, j, 0))

            elif arr[i][j] == '1':
                new_arr[i][j] = '-2'

    while q:
        y, x, cnt = q.popleft()
        cnt += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_spread(ny, nx, cnt):
                q.append((ny, nx, cnt))
    

spread()

for i in range(n):
    print(' '.join(new_arr[i]))