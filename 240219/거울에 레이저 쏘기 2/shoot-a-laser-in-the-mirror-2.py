N = int(input())
info = [input() for _ in range(N)]
K = int(input()) - 1
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
idx = K//N
y = x = cnt = 0
cnt, temp_i = 1, 3

for _ in range(K):
    ny = y + direction[temp_i][0]
    nx = x + direction[temp_i][1]
    if 0 <= ny < N and 0 <= ny < N:
        y, x = ny, nx
    else:
        temp_i = (temp_i + 1) % 4
        y += direction[temp_i][0]
        x += direction[temp_i][1]

while 0 <= y < N and 0 <= y < N:
    cnt += 1
    if info[y][x] == '/':
        idx = 3 - idx
    elif idx % 2:
        idx -= 1
    else:
        idx += 1
    
    y += direction[idx][0]
    x += direction[idx][1]

print(cnt)