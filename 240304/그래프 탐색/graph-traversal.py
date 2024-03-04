N, M = map(int, input().split())
link_info = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    link_info[x].append(y)
    link_info[y].append(x)


def check_destination(node):
    for next in link_info[node]:
        if not visited[next]:
            visited[next] = True
            check_destination(next)

visited[1] = True
check_destination(1)

print(visited.count(True) - 1)