N = int(input())
direction = {
    'W': (-1, 0),
    'S': (0, -1),
    'N': (0, 1),
    'E': (1, 0),
}

key, duration = input().split()
duration = int(duration)
dx, dy = direction[key]
y, x = dy * duration, dx * duration
time = duration

for _ in range(N-1):
    key, duration = input().split()
    duration = int(duration)
    dx, dy = direction[key]
    dx *= duration
    dy *= duration

    if x == 0:
        if dy * y < 0 and abs(dy) >= abs(y):
            print(time+abs(y))
            break
    elif y == 0:
        if dx * x < 0 and abs(dx) >= abs(x):
            print(time+abs(x))
            break
    
    time += duration
    x += dx
    y += dy

else:
    print(-1)