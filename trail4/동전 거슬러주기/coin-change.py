N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.
coins.sort()
remain = [M+1] * (M+1)
remain[0] = 0
for i in range(1, M+1):
    for coin in coins:
        if coin > i:
            break
        remain[i] = min(remain[i-coin] + 1, remain[i])

print(-1 if remain[-1] == M+1 else remain[-1])
