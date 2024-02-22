n, r, c = map(lambda x: int(x)-1, input().split())
n += 1
arr = [list(map(int, input().split())) for _ in range(n)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
numbers = []

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

while True:
    now = arr[r][c]
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if in_range(nr, nc) and now < arr[nr][nc]:
            r, c = nr, nc
            numbers.append(str(now))
            break
    else:
        numbers.append(str(now))
        break

print(' '.join(numbers))