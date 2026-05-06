n = int(input())
max_income = [0] * (n+2)

for i in range(n):
    t, p = map(int, input().split())
    max_income[i+1] = max(max_income[i:i+2])
    if i+t < n+1:
        max_income[i+t+1] = max(max_income[i+1] + p, max_income[i+t+1])


print(max(max_income[-2:]))



