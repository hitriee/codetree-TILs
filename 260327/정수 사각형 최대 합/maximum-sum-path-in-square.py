n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
acc = [grid[i][:] for i in range(n)]

for i in range(1, n):
    acc[i][0] += acc[i-1][0]
    acc[0][i] += acc[0][i-1]


for i in range(1, n):
    for j in range(1, n):
        acc[i][j] += max(acc[i-1][j], acc[i][j-1])

print(acc[-1][-1])

