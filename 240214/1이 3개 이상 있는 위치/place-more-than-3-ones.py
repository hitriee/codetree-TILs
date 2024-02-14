n = int(input())
arr = [input().split() for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt_position = 0

for y in range(n):
    for x in range(n):
        cnt_near = 0
        for dx, dy in zip(dxs, dys):
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == '1':
                cnt_near += 1
        if cnt_near >= 3:
            cnt_position += 1

print(cnt_position)