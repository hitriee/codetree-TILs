from sys import stdin


def int_input():
    return map(int, stdin.readline().split())


N, M = int_input()
arr = [list(int_input()) for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
max_total = 0
visited = set()

def dfs(level, total):
    global max_total

    if level == 4:
        if max_total < total:
            max_total = total
        return
    
    new_level = level + 1
    temp = set(visited)
    for y, x in temp:
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    dfs(new_level, total + arr[ny][nx])
                    visited.remove((ny, nx))
                

for i in range(N):
    for j in range(M):
        visited.add((i, j))
        dfs(1, arr[i][j])
        visited.remove((i, j))


print(max_total)