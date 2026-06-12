from collections import deque


def sort_order(position):
    y, x = position
    return (-amount[y][x], y, x)


def bfs(visited, target, initial):
    q.append(initial)
    group = [initial]
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if favorite[ny][nx] == target and not visited[ny][nx]:
                    group.append((ny, nx))
                    q.append((ny, nx))
                    visited[ny][nx] = True

    return group


# 아침 & 점심
def make_group():
    visited = [[False] * N for _ in range(N)]
    leaders = [[] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                target = favorite[i][j]
                visited[i][j] = True
                group = bfs(visited, target, (i, j))
                leaders[num_to_i[target]].append(find_leader(group))
    return leaders


# 각 그룹에서의 리더 찾기
def find_leader(group):
    group.sort(key=sort_order)
    y, x = group[0]
    amount[y][x] += len(group)
    return (y, x)


# 신앙 전파
def spread(leaders):
    visited = [[False] * N for _ in range(N)]
    for group in leaders:
        group.sort(key=sort_order)
        for y, x in group:
            if not visited[y][x]:
                value = amount[y][x]
                d, ny, nx, target = value % 4, y, x, favorite[y][x]
                value -= 1
                amount[y][x] = 1
                visited[y][x] = True

                while 0 <= ny < N and 0 <= nx < N and value > 0:
                    if favorite[ny][nx] != target:
                        visited[ny][nx] = True
                        new_value = amount[ny][nx]
                        if value > new_value:
                            value -= (new_value + 1)
                            amount[ny][nx] += 1
                            favorite[ny][nx] = target
                        else:
                            amount[ny][nx] += value
                            value = 0
                            favorite[ny][nx] |= target

                    ny += dy[d]
                    nx += dx[d]


# 신앙심 합 계산
def calc_total():
    total = [0] * 8
    for i in range(N):
        for j in range(N):
            total[favorite[i][j]] += amount[i][j]

    answer = []
    for idx in order:
        answer.append(str(total[idx]))
    return ' '.join(answer)


food_to_num = {'T': 1, 'C': 2, 'M': 4}

N, T = map(int, input().split())
favorite = [list(map(lambda x: food_to_num[x], input())) for _ in range(N)]
amount = [list(map(int, input().split())) for _ in range(N)]
order = [7, 3, 5, 6, 4, 2, 1]
num_to_i = {1:0, 2:0, 4:0, 6:1, 5:1, 3:1, 7:2}
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
q = deque()

for _ in range(T):
    leaders = make_group()
    spread(leaders)
    print(calc_total())