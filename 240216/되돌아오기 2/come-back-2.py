commands = input()
N = len(commands)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x = idx = 0
y = 1
for i in range(1, N):
    command = commands[i]
    if command == 'F':
        x += dx[idx]
        y += dy[idx]
        if y == x == 0:
            print(i+1)
            break
    elif command == 'R':
        idx = (idx + 1) % 4
    else:
        idx = (idx - 1) % 4
else:
    print(-1)