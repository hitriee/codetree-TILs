n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
for i in range(1, n):
    grid[i][0] = max(grid[i][0], grid[i-1][0])
    grid[0][i] = max(grid[0][i], grid[0][i-1])

for i in range(1, n):
    for j in range(1, n):
        grid[i][j] = max(min(grid[i-1][j], grid[i][j-1]), grid[i][j])

print(grid[-1][-1])