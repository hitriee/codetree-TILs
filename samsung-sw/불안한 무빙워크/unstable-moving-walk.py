N, K = map(int, input().split())
stability = list(map(int, input().split()))
cnt = idx = 0
M = 2 * N
visited = [False] * M
# 0번 칸에 올라가서 N-1 칸에서 내림
# 사람이 칸에 올라가거나 이동하면 안정성 1 감소 - 안정성 0인 칸에 올라갈 수 없음
while True:
    cnt += 1
    # 무빙워크 한 칸 회전
    idx = (idx - 1) % M

    last = (idx + N - 1) % M
    # N-1에 사람 위치하면 즉시 내림
    if visited[last]:
        visited[last] = False

    # 가장 먼저 올라간 사람부터 한 칸 이동 (사람이 이미 있거나 안정성 0인 경우 제외)
    limit = (idx + N - 2)
    for i in range(limit, idx-1, -1):
        j = i % M
        k = (i+1) % M
        if visited[j] and not visited[k] and stability[k] > 0:
            visited[j] = False
            visited[k] = True
            stability[k] -= 1
    # N-1에 사람 위치하면 즉시 내림
    if visited[last]:
        visited[last] = False

    # 0번 칸에 사람이 없고 안정성 > 0이면 사람 더 올림
    if not visited[idx] and stability[idx] > 0:
        visited[idx] = True
        stability[idx] -= 1

    # 안정성이 0인 칸이 K개 이상이면 과정 종료
    zero_cnt = 0
    for i in range(M):
        if stability[i] == 0:
            zero_cnt += 1

    if zero_cnt >= K:
        break

print(cnt)