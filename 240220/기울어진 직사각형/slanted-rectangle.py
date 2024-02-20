n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dx, dy = [1, 1, -1, -1], [1, -1, -1, 1]
max_total = 0

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

for i in range(1, n-1):
    for j in range(n-2):
        initial = arr[i][j]
        y, x = i+1, j+1
        d = 1
        while in_range(y, x):
            initial += arr[y][x]
            ny, nx = y-1, x+1
            ni, nj = i-1, j+1
            total = initial
            while in_range(ni, nj) and in_range(ny, nx):
                total += arr[ni][nj] + arr[ny][nx]
                ni -= 1
                ny -= 1
                nj += 1
                nx += 1
                
            ni += 1
            nj -= 1
            nx -= 2
            while ni != ny:
                total += arr[ny][nx]
                ny -= 1
                nx -= 1
                
            if max_total < total:
                max_total = total
            else:
                break
                
            y += 1
            x += 1

print(max_total)