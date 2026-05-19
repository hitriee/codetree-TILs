n = int(input())

# Please write your code here.
if n == 1:
    print(1)
else:
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        cnt = 0
        for j in range(i):
            cnt += dp[j] * dp[i-1-j]
        dp[i] = cnt
    
    print(dp[-1])