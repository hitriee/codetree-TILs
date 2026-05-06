n = int(input())
max_income = [0] * (n+1)
t, p = map(int, input().split())
if t < n+1:
    max_income[t] = p


for i in range(1, n):
    t, p = map(int, input().split())
    if max_income[i-1] > max_income[i]:
        max_income[i] = max_income[i-1]
    if i+t < n+1:
        max_income[i+t] = max(max_income[i] + p, max_income[i+t])

print(max(max_income))


