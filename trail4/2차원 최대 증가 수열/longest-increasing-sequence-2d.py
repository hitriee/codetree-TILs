N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
max_cnt = [[0] * M for _ in range(N)]
max_cnt[0][0] = 1

# Please write your code here.
for i in range(N):
    for j in range(M):
        if max_cnt[i][j] != 0:
            before, new_cnt = grid[i][j], max_cnt[i][j] + 1
            for y in range(i+1, N):
                for x in range(j+1, M):
                    if grid[y][x] > before and max_cnt[y][x] < new_cnt:
                        max_cnt[y][x] = new_cnt


# print(max_cnt)
print(max([max(max_cnt[i]) for i in range(N)]))