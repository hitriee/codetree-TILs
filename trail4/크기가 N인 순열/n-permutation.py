n = int(input())
path = []
visited = [False] * (n+1)

def dfs(level):
    if level == n:
        print(*path)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            dfs(level+1)
            path.pop()
            visited[i] = False

dfs(0)
