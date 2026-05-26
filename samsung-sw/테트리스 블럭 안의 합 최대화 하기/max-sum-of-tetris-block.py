from sys import stdin
from collections import deque


def int_input():
    return map(int, stdin.readline().split())


N, M = int_input()
arr = [list(int_input()) for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
q = deque()
max_total = 0

for i in range(N):
    for j in range(M):
        q.append((1, arr[i][j], {(i, j)}))
        while q:
            cnt, total, visited = q.popleft()
            if cnt == 4:
                if max_total < total:
                    max_total = total
            else:
                new_cnt = cnt + 1
                for y, x in visited:
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < N and 0 <= nx < M:
                            if (ny, nx) not in visited:
                                q.append((new_cnt, total + arr[ny][nx], visited | {(ny, nx)}))

print(max_total)