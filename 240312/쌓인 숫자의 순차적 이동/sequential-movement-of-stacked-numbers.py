from collections import deque

n, m = map(int, input().split())
max_nums = []
position = [[] for _ in range(n*n+1)]
total_nums = [[deque() for _ in range(n)] for _ in range(n)]
dy, dx = [1, 1, 1, 0, 0, -1, -1, -1], [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    numbers = list(map(int, input().split()))
    max_nums.append(numbers)
    for j in range(n):
        number = numbers[j]
        position[number] = (i, j)
        total_nums[i][j].append(number)

commands = tuple(map(int, input().split()))

for command in commands:
    y, x = position[command]
    max_num = 0
    for i in range(8):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < n and max_num < max_nums[ny][nx]:
            max_num = max_nums[ny][nx]
            last_y, last_x = ny, nx
    
    if max_num:
        temp = []
        for _ in range(len(total_nums[y][x])):
            num = total_nums[y][x].popleft()
            position[num] = (last_y, last_x)
            temp.append(num)
            if num == command:
                break
        total_nums[last_y][last_x].extendleft(temp[::-1])
        max_nums[last_y][last_x] = max(max_nums[last_y][last_x], *temp)
        max_nums[y][x] = max(total_nums[y][x]) if total_nums[y][x] else 0


for i in range(n):
    for j in range(n):
        if total_nums[i][j]:
            print(*total_nums[i][j])
        else:
            print('None')