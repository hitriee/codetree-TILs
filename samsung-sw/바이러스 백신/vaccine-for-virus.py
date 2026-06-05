def main():
    from collections import deque

    def choose_hospital(level, start):
        nonlocal min_time

        if level == M:
            duration = vaccinate()
            if min_time > duration:
                # print(chosen)
                # print(min_time, duration)
                min_time = duration
            return
        
        new_level = level + 1
        for i in range(start, K):
            chosen.append((*hospitals[i], 0))
            choose_hospital(new_level, i+1)
            chosen.pop()
    
    def vaccinate():
        total = virus_cnt
        q = deque(chosen)
        visited = [[False] * N for _ in range(N)]
        duration = 0

        while q:
            y, x, duration = q.popleft()
            
            new_duration = duration + 1
            
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    val = arr[ny][nx]
                    if val != '1' and not visited[ny][nx]:
                        if val == '0':
                            total -= 1
                            if total == 0:
                                return new_duration
                            
                        visited[ny][nx] = True
                        q.append((ny, nx, new_duration))

        return 3000

    


    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    # 0 바이러스 1 벽 2 병원
    # M개의 병원을 적절히 골라 모든 바이러스를 없애는 데 필요한 최소 시간
    min_time = 3000
    virus_cnt = 0
    hospitals, chosen = [], []
    dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)

    for i in range(N):
        for j in range(N):
            val = arr[i][j]
            if val == '0':
                virus_cnt += 1
            elif val == '2':
                hospitals.append((i, j))

    if virus_cnt == 0:
        return 0

    K = len(hospitals)
    choose_hospital(0, 0)

    return min_time if min_time < 3000 else -1

print(main())