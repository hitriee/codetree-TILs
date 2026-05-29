N, M = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
weight_to_max_val = [0] * (M+1)

for w, v in jewels:
    temp = list(weight_to_max_val)
    for i in range(w, M+1):
        temp[i] = max(temp[i], weight_to_max_val[i-w] + v)
    weight_to_max_val = list(temp)


print(weight_to_max_val[-1])
