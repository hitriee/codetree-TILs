n, m, k = map(int, input().split())
arr = [input().split() for _ in range(n)]
block_i = n-1

for j in range(k-1, m+k-1):
    for i in range(n-1):
        if arr[i+1][j] == '1':
            if block_i > i:
                block_i = i
            break
    else:
        break

for j in range(k-1, m+k-1):
    arr[block_i][j] = '1'

for i in range(n):
    print(' '.join(arr[i]))