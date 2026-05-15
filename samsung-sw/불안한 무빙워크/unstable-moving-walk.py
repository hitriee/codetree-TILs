N, K = map(int, input().split())
stability = list(map(int, input().split()))
cnt = idx = 0
M = 2*N
visited = [False] * M

while True:
    cnt += 1
    stability.insert(0, stability.pop())
    visited.insert(0, visited.pop())
    
    if visited[N-1]:
        visited[N-1] = False
    
    for i in range(N-2, -1, -1):
        if visited[i] and not visited[i+1] and stability[i+1] > 0:
            visited[i] = False
            visited[i+1] = True
            stability[i+1] -= 1

    if visited[N-1]:
        visited[N-1] = False
    
    if not visited[0] and stability[0] > 0:
        visited[0] = True
        stability[0] -= 1

    zero_cnt = 0
    for i in range(M):
        if stability[i] == 0:
            zero_cnt += 1
    
    if zero_cnt >= K:
        break


print(cnt)
