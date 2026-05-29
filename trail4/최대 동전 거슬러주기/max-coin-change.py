N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.
cnt = [-1] * (M+1)
cnt[0] = 0
coins.sort()

for i in range(1, M+1):
    for coin in coins:
        if i < coin:
            break
        if cnt[i - coin] > -1:
            cnt[i] = max(cnt[i], cnt[i-coin] + 1)

print(cnt[-1])
