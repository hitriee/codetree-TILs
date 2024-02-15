def find_time():

    N = int(input())
    direction = {
        'W': (-1, 0),
        'S': (0, -1),
        'N': (0, 1),
        'E': (1, 0),
    }

    y = x = time = 0

    for _ in range(N):
        key, duration = input().split()
        duration = int(duration)
        dx, dy = direction[key]
        for _ in range(duration):
            x += dx
            y += dy
            time += 1
            if x == y == 0:
                return time
    return -1

print(find_time())