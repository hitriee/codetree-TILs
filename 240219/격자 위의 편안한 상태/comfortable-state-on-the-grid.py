N, M = map(int, input().split())
arr = [[0] * N for _ in range(N)]
dr, dc = [-1, 0, -1, -2], [0, -1, -2, -1]
for _ in range(M):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
    cnt = 0
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
            cnt += 1
    print(1 if cnt == 3 else 0)