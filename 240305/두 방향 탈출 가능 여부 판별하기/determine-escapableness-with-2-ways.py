n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = '0'

def can_go(y, x):
    if 0 <= y < n and 0 <= x < m and arr[y][x] == '1' and not visited[y][x]:
        visited[y][x] = True
        return True
    return False

def dfs(y, x):
    global result

    if result == '1':
        return

    if y == n-1 and x == m-1:
        result = '1'
        return
    
    if can_go(y+1, x):
        dfs(y+1, x)
    if can_go(y, x+1):
        dfs(y, x+1)

dfs(0, 0)
print(result)