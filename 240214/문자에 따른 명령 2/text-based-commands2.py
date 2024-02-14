command = input()
y = x = direction = 0
direction_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for alp in command:
    if alp == 'L':
        direction = (direction-1)%4
    elif alp == 'R':
        direction = (direction+1)%4
    else:
        y += direction_list[direction][0]
        x += direction_list[direction][1]

print(x, y)