n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]

def can_go(y, x):
    if 0 <= y < n and 0 <= x < m and arr[y][x] == '1':
        return True
    return False

def dfs(y, x):
    if y == n-1 and x == m-1:
        return 1
    
    result = 0
    
    if can_go(y+1, x):
        result = dfs(y+1, x)
    if can_go(y, x+1):
        result = result or dfs(y, x+1)
    
    return result

print(dfs(0, 0))