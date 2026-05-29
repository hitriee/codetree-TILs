N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.
cnt = [-1] * (M+1)
cnt[0] = 0
coins.sort()

for i in range(1, M+1):
    for coin in coins:
        before = i - coin
        if before < 0:
            break
        if cnt[before] > -1:
            cnt[i] = max(cnt[i], cnt[before] + 1)

print(cnt[-1])
