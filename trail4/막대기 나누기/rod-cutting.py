n = int(input())
profit = [0] + list(map(int, input().split()))

# Please write your code here.

for j in range(1, n+1):
    value = profit[j]
    for i in range(j, n+1):
        if profit[i-j] != 0:
            profit[i] = max(profit[i], profit[j] + profit[i-j])

print(profit[-1])