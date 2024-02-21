n = int(input())
arr = [input().split() for _ in range(n)]
r, c = map(lambda x: int(x)-1, input().split())
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]

def bomb():
    limit = int(arr[r][c]) - 1
    arr[r][c] = '0'

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        for _ in range(limit):
            if 0 <= nr < n and 0 <= nc < n:
                arr[nr][nc] = '0'
            else:
                break
            nr += dr[i]
            nc += dc[i]

def gravity(j):
    bottom = n-1
    while True:
        while arr[bottom][j] != '0':
            bottom -= 1
            if bottom <= 0:
                return
        
        top = bottom - 1
        while arr[top][j] == '0':
            top -= 1
            if top < 0:
                return

        arr[top][j], arr[bottom][j] = arr[bottom][j], arr[top][j]


if n > 1:
    bomb()
    for j in range(n):
        gravity(j)

    for i in range(n):
        print(' '.join(arr[i]))
else:
    print('0')