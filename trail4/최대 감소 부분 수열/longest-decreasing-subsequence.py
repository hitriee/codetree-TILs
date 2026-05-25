N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_len = [0] * N
max_len[0] = 1

for i in range(1, N):
    num = arr[i]
    len_arr = [0]
    for j in range(i):
        if arr[j] > num:
            len_arr.append(max_len[j])
    max_len[i] = max(len_arr) + 1

print(max(max_len))