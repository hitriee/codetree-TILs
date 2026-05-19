n = int(input())

# Please write your code here.
if n == 1:
    print(2)

else:
    dp = [0] * (n+1)
    div_num = int(1e9) + 7
    dp[0], dp[1], dp[2] = 1, 2, 7
    for i in range(3, n+1):
        dp[i] = (sum(dp[:i]) * 2 + dp[i-2]) % div_num
    
    print(dp[-1])
