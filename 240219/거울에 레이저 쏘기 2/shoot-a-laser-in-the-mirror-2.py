N = int(input())
info = [input() for _ in range(N)]
K = int(input()) - 1
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
idx, cnt = K//N, 0

if idx == 0:
    y, x = 0, K
elif idx == 1:
    y, x = K%N, N-1
elif idx == 2:
    y, x = N-1, N-1-(K%N)
else:
    y, x = N-1-(K%N), 0

while 0 <= y < N and 0 <= x < N:
    cnt += 1
    if info[y][x] == '\\':
        idx = 3 - idx
    elif idx % 2:
        idx -= 1
    else:
        idx += 1
    
    y += direction[idx][0]
    x += direction[idx][1]

print(cnt)