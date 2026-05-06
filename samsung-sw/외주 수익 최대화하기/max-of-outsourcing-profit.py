n = int(input())
max_income = [0] * (n+1)

for i in range(n):
    t, p = map(int, input().split())
    max_income[i] = max(max_income[:i+1])
    if i+t < n+1:
        max_income[i+t] = max(max_income[i] + p, max_income[i+t])


print(max(max_income))



