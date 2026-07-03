def int_input():
    return map(int, input().split())

def grow_or_dead():
    dead_virus, five_arr = [], []
    for i in range(N):
        for j in range(N):
            kind_of = virus[i][j]
            if kind_of:
                years = sorted(kind_of)
                new_kind_of = {}
                for year in years:
                    val, cnt, new_year = arr[i][j], kind_of[year], year+1
                    if val >= cnt * year:
                        # 양분 섭취
                        arr[i][j] -= year * cnt
                        new_kind_of[new_year] = cnt
                        if new_year % 5 == 0:
                            five_arr.append((i, j, cnt))
                    else:
                        quot = arr[i][j] // year
                        if quot != 0:
                            # 양분 섭취
                            arr[i][j] -= year * quot
                            new_kind_of[new_year] = quot
                            if new_year % 5 == 0:
                                five_arr.append((i, j, quot))
                        dead_virus.append((i, j, (year // 2) * (cnt - quot)))
                virus[i][j] = dict(new_kind_of)
    
    for i, j, val in dead_virus:
        arr[i][j] += val
    
    return five_arr

def spread(five_arr):
    for r, c, cnt in five_arr:
        for i in range(8):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                virus[nr][nc][1] = virus[nr][nc].get(1, 0) + cnt

def plus():
    for i in range(N):
        for j in range(N):
            arr[i][j] += plus_arr[i][j]

def count_virus():
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += sum(virus[i][j].values())
    return cnt



N, M, K = int_input()
plus_arr = [list(int_input()) for _ in range(N)]
arr = [[5] * N for _ in range(N)]
dr, dc = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)
virus = [[{} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, year = int_input()
    virus[r-1][c-1][year] = virus[r-1][c-1].get(year, 0) + 1

for _ in range(K):
    five_arr = grow_or_dead()
    spread(five_arr)
    plus()

print(count_virus())