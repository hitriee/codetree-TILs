N, M = map(int, input().split())
arr = [[0] * (N+2) for _ in range(N+2)]
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(M):
    r, c = map(int, input().split())
    arr[r][c] = 1
    cnt = 0
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if arr[nr][nc] == 1:
            cnt += 1
    print(1 if cnt == 3 else 0)