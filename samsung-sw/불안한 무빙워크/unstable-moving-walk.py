N, K = map(int, input().split())
stability = list(map(int, input().split()))
cnt = idx = 0
M = 2*N
visited = [False] * M
# 0번 칸에 올라가서 N-1 칸에서 내림
# 사람이 칸에 올라가거나 이동하면 안정성 1 감소 - 안정성 0인 칸에 올라갈 수 없음
while True:
    cnt += 1
    # 무빙워크 한 칸 회전
    stability = stability[-1:] + stability[:-1]
    visited = visited[-1:] + visited[:-1]

    # N-1에 사람 위치하면 즉시 내림
    if visited[N-1]:
        visited[N-1] = False
    
    # 가장 먼저 올라간 사람부터 한 칸 이동 (사람이 이미 있거나 안정성 0인 경우 제외)
    for i in range(N-2, -1, -1):
        if visited[i] and not visited[i+1] and stability[i+1] > 0:
            visited[i] = False
            visited[i+1] = True
            stability[i+1] -= 1
    
    # N-1에 사람 위치하면 즉시 내림
    if visited[N-1]:
        visited[N-1] = False
    
    # 0번 칸에 사람이 없고 안정성 > 0이면 사람 더 올림
    if not visited[0] and stability[0] > 0:
        visited[0] = True
        stability[0] -= 1
        
    # 안정성이 0인 칸이 K개 이상이면 과정 종료
    zero_cnt = 0
    for i in range(M):
        if stability[i] == 0:
            zero_cnt += 1
    
    if zero_cnt >= K:
        break


print(cnt)