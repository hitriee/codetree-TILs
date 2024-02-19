n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
max_total = 0

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

for i in range(1, n-1):
    for j in range(n-1):
        d = 1
        while True:
            y, x = i+d, j+d
            if 0 <= y < n and 0 <= x < n:
                total = arr[i][j] + arr[y][x]
                ni, nj = i-1, j+1
                ny, nx = y-1, x+1
                while in_range(ni, nj) and in_range(ny, nx):
                    total += arr[ni][nj] + arr[ny][nx]
                    ni -= 1
                    ny -= 1
                    nj += 1
                    nx += 1
                    
                if max_total < total:
                    max_total = total
            else:
                break
            d += 1

print(max_total)