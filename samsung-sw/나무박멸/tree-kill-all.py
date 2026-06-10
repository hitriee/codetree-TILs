from sys import stdin

def int_input():
    return map(int, stdin.readline().split())

# 성장 & 번식
def grow():
    temp = [arr[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if temp[i][j] > 0:
                around_cnt = 0
                path = []
                for di, dj in straight:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N:
                        val = temp[ni][nj]
                        if val > 0:
                            around_cnt += 1
                        elif val == 0 and limit_info[ni][nj] == max_year:
                            path.append((ni, nj))
                arr[i][j] += around_cnt
                if path:
                    plus = arr[i][j] // len(path)
                    for ni, nj in path:
                        arr[ni][nj] += plus
                
# 제초제 사라짐
def remove():
    for i in range(N):
        for j in range(N):
            if limit_info[i][j] <= year:
                limit_info[i][j] = max_year

# 제초제 뿌릴 위치 찾기
def find_position():
    max_cnt = y = x = 0
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            if cnt > 0:
                for di, dj in cross:
                    ni, nj = i, j
                    for _ in range(K):
                        ni += di
                        nj += dj
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                            cnt += arr[ni][nj]
                        else:
                            break

                if cnt > max_cnt:
                    max_cnt, y, x = cnt, i, j
    
    return (max_cnt, y, x)

# 제초제 뿌림
def spray():
    max_cnt, y, x = find_position()
    
    new_year = year + C
    limit_info[y][x] = new_year
    if arr[y][x] > 0:
        arr[y][x] = 0
        for dy, dx in cross:
            ny, nx = y, x
            for _ in range(K):
                ny += dy
                nx += dx
                if 0 <= nx < N and 0 <= ny < N:
                    limit_info[ny][nx] = new_year
                    if arr[ny][nx] <= 0:
                        break
                    arr[ny][nx] = 0
                else:
                    break
    return max_cnt

N, M, K, C = int_input()
arr = [list(int_input()) for _ in range(N)]
removed_cnt = 0

straight = [(-1, 0), (0, -1), (1, 0), (0, 1)]
cross = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

max_year = M + C
limit_info = [[max_year] * N for _ in range(N)]

for year in range(M):
    grow()
    remove()
    removed_cnt += spray()

print(removed_cnt)
