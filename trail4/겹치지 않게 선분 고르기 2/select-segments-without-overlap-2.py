n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines.sort()

cnt = [0] * n
cnt[0] = 1

for i in range(1, n):
    start = lines[i][0]
    max_val = 1
    for j in range(i):
        end = lines[j][1]
        if start > end:
            max_val = max(cnt[j] + 1, max_val)
    cnt[i] = max_val

print(max(cnt))