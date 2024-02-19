n, m = map(int, input().split())
rectangle = [tuple(map(int, input().split())) for _ in range(n)]
max_size = -1
check = [[-1] * m for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(m-1, -1, -1):
        if rectangle[i][j] > 0:
            cnt += 1
            check[i][j] = cnt
        else:
            cnt = 0

for i in range(n):
    for j in range(m):
        horizontal = check[i][j]
        if horizontal > 0:
            vertical = 2
            if max_size < horizontal:
                max_size = horizontal
            for ni in range(i+1, n):
                horizontal = min(horizontal, check[ni][j])
                size = vertical * horizontal
                if max_size < size:
                    max_size = size
                vertical += 1

print(max_size)