n, m, k = map(int, input().split())
arr = [input().split() for _ in range(n)]
block_i = n

for j in range(k-1, m+k-1):
    for i in range(1, n):
        if arr[i][j] == '1':
            if block_i > i-1:
                block_i = i-1
            break
    else:
        block_i = n-1
        break

for j in range(k-1, m+k-1):
    arr[block_i][j] = '1'

for i in range(n):
    print(' '.join(arr[i]))