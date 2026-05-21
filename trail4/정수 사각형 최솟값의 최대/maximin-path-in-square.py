n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
for i in range(1, n):
    grid[i][0] = min(grid[i-1][0], grid[i][0])
    grid[0][i] = min(grid[0][i-1], grid[0][i])

for i in range(1, n):
    for j in range(1, n):
        grid[i][j] = min(grid[i][j], max(grid[i-1][j], grid[i][j-1]))

print(grid[-1][-1])