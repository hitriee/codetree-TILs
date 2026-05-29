n = int(input())
profit = [0] + list(map(int, input().split()))

# Please write your code here.
max_profit = [0] * (n+1)
for i in range(1, n+1):
    max_profit[i] = profit[i]

for j in range(1, n+1):
    value = profit[j]
    for i in range(j, n+1):
        if max_profit[i-j] != 0:
            max_profit[i] = max(max_profit[i], max_profit[j] + max_profit[i-j])

print(max_profit[-1])