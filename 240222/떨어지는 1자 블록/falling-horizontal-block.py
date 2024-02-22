n, m, k = map(int, input().split())
arr = [input().split() for _ in range(n)]
block_i = n

for j in range(k-1, m+k-1):
    for i in range(n-1, 0, -1):
        if arr[i][j] == '0':
            if block_i > i:
                block_i = i
            break


arr[block_i][k-1:m+k-1] = ['1'] * m

for i in range(n):
    print(' '.join(arr[i]))