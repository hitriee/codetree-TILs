n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    max_len = [0] * n
    max_len[0] = 1

    for i in range(1, n):
        now = arr[i]
        temp = [0]
        for j in range(i):
            if arr[j] < now:
                temp.append(max_len[j])

        max_len[i] = max(temp) + 1
    
    print(max(max_len))