from collections import deque

def int_input():
    return map(int, input().split())

# 3x3 격자 선택
def find_arr():
    final_y = final_x = 5
    max_val, degree_i = 0, 4
    total_path = []
    for x in range(1, 4):
        for y in range(1, 4):
            arr = [area[k][:] for k in range(5)]
            position = [(y+dy[k], x+dx[k]) for k in range(8)]
            for i in range(3):
                rotate(position, arr)
                path = find_path(arr)
                val = len(path)
                if max_val < val:
                    final_y, final_x, max_val, degree_i = y, x, val, i
                    total_path = path[:]
                elif max_val == val:
                    if degree_i > i:
                        final_y, final_x, degree_i = y, x, i
                        total_path = path[:]
                    elif degree_i == i:
                        if final_x > x:
                            final_y, final_x = y, x
                            total_path = path[:]
                        elif final_x == x and final_y > y:
                            final_y = y
                            total_path = path[:]
    
    path = apply_new_arr(final_y, final_x, degree_i+1)
    renew(total_path)

    return max_val


        

# 시계 방향 회전
def rotate(position, arr):
    before = [arr[i][:] for i in range(5)]
    for i in range(8):
        y, x = position[i]
        ny, nx = position[(i+2) % 8]
        arr[ny][nx] = before[y][x]


# 유물 위치 찾기
def find_path(arr):
    total_path = []
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                visited[i][j] = True
                target = arr[i][j]
                path = [(i, j)]
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    for k in range(1, 8, 2):
                        ny, nx = y+dy[k], x+dx[k]
                        if 0 <= ny < 5 and 0 <= nx < 5:
                            if arr[ny][nx] == target and not visited[ny][nx]:
                                path.append((ny, nx))
                                q.append((ny, nx))
                                visited[ny][nx] = True
                if len(path) >= 3:
                    total_path.extend(path)

    return total_path

# 새 배열 적용
def apply_new_arr(y, x, limit):
    position = [(y+dy[k], x+dx[k]) for k in range(8)]
    for _ in range(limit):
        rotate(position, area)

# 유물 삭제 & 빈 부분 치우기
def renew(path):
    global part_of_i

    path.sort(lambda x: (x[1], -x[0]))

    for y, x in path:
        area[y][x] = part_of[part_of_i]
        part_of_i += 1


# 반복 횟수, 유물 조각 개수
K, M = int_input()
area = [list(int_input()) for _ in range(5)]
part_of = list(int_input())
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
values, q = [], deque()
part_of_i = 0

for _ in range(K):
    value = find_arr()
    if value == 0:
        break
    
    while True:
        total_path = find_path(area)
        if total_path:
            value += len(total_path)
            renew(total_path)
        else:
            break
    values.append(str(value))
    

print(' '.join(values))
