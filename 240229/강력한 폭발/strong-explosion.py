n = int(input())
arr = [input().split() for _ in range(n)]
position = []
max_cnt = 0
affected = [[False] * n for _ in range(n)]
dy = [(-2, -1, 1, 2), (-1, 0, 0, 1), (-1, -1, 1, 1)]
dx = [(0, 0, 0, 0), (0, -1, 1, 0), (-1, 1, -1, 1)]


for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            position.append((i, j))
            affected[i][j] = True

limit = len(position)
def bomb(level=0, cnt=limit):
    global max_cnt

    if level == limit:
        if max_cnt < cnt:
            max_cnt = cnt
        return
    
    y, x = position[level]
    for i in range(3):
        new_cnt = cnt
        new_position = []
        for j in range(4):
            ny, nx = y+dy[i][j], x+dx[i][j]
            if 0 <= ny < n and 0 <= nx < n and not affected[ny][nx]:
                affected[ny][nx] = True
                new_cnt += 1
                new_position.append((ny, nx))
        bomb(level+1, new_cnt)
        for ny, nx in new_position:
            affected[ny][nx] = False

bomb()
print(max_cnt)