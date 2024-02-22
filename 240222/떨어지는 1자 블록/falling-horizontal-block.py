n, m, k = map(int, input().split())
arr = [input() for _ in range(n)]
block_i = n-1

for j in range(k-1, m+k-1):
    for i in range(1, n):
        if arr[i][2*j] == '1':
            if block_i > i-1:
                block_i = i-1
            break
    else:
        break

arr[block_i] = arr[block_i][:2*(k-1)] + ' '.join(['1']*m) + arr[block_i][2*(m+k-2)+1:]

for i in range(n):
    print(arr[i])