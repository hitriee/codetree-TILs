n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
max_total = 0
def in_range(ny, nx):
    return 0 <= ny < n and 0 <= nx < m

for y in range(n):
    for x in range(m):
        one = arr[y][x]
        for i in range(3):
            ny, nx = y + dy[i], x + dx[i]
            if in_range(ny, nx):
                two = one + arr[ny][nx]
                for j in range(i+1, 4):
                    nny, nnx = y + dy[j], x + dx[j]
                    if in_range(nny, nnx):
                        total = two + arr[nny][nnx]
                        if total > max_total:
                            max_total = total

print(max_total)