N = int(input())
y = x = 0
converted_direction = {
    'N': (1, 0),
    'E': (0, 1),
    'S': (-1, 0),
    'W': (0, -1),
}
for _ in range(N):
    direction, step = input().split()
    step = int(step)
    y += converted_direction[direction][0] * step
    x += converted_direction[direction][1] * step

print(x, y)