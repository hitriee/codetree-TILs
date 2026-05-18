def find_position(n, *favorite):
    favorite = set(favorite)
    # 우선 순위 높은 칸 탑승
    max_cnt = max_empty = -1
    y = x = N
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt = empty = 0
                for k in range(4):
                    ni, nj = i + dy[k], j + dx[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        num = arr[ni][nj]
                        if num == 0:
                            empty += 1
                        elif num in favorite:
                            cnt += 1
                # 1. 인접 칸 중 좋아하는 친구의 수가 가장 많은 위치로 이동
                if cnt > max_cnt:
                    max_cnt, max_empty, y, x = cnt, empty, i, j
                elif cnt == max_cnt:
                    # 2. 1번 조건 여러 곳이면 인접 칸 중 비어있는 칸의 수가 가장 많은 위치로
                    if empty >= max_empty:
                        # 3. 2번 조건 여러 곳이면 행 작은 위치
                        # 4. 3번 조건 여러 곳이면 열 작은 위치
                        max_empty, y, x = empty, i, j
                        

    arr[y][x] = n
    students.append((n, favorite))

# 모든 학생들이 놀이기구에 탑승한 이후의 최종 점수
def calc_total():
    score = [int(10 ** (i - 1)) for i in range(5)]
    total = 0

    for y in range(N):
        for x in range(N):
            num = arr[y][x]
            cnt = 0
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if arr[ny][nx] in students[num - 1][1]:
                        cnt += 1
            total += score[cnt]
    return total




# ----
N = int(input())

# 놀이기구
arr = [[0] * N for _ in range(N)]
students = []
dy, dx = (-1, 0, 0, 1), (0, -1, 1, 0)

for _ in range(N*N):
    # 탑승 번호, 좋아하는 학생 번호
    find_position(*map(int, input().split()))

students.sort()

# 최종점수는 각 학생마다 인접한 곳에 앉아 있는 좋아하는 친구의 수로 결정됨
print(calc_total())