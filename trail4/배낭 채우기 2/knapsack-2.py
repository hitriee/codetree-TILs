N, M = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
max_val = [0] * (M+1)
for w, v in jewels:
    for i in range(w, M+1):
        max_val[i] = max(max_val[i], max_val[i-w] + v)

print(max_val[-1])
