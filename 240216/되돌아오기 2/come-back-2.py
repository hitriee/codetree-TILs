commands = input()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x = y = idx = time = 0
for command in commands:
    time += 1
    if command == 'F':
        x += dx[idx]
        y += dy[idx]
        if y == x == 0:
            print(time)
            break
    elif command == 'R':
        idx = (idx + 1) % 4
    else:
        idx = (idx - 1) % 4
else:
    print(-1)