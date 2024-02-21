n, t = map(int, input().split())
belt = [input().split() for _ in range(3)]

for _ in range(t):
    last_numbers = [belt[i][-1] for i in range(3)]
    for j in range(n-1, 0, -1):
        for i in range(3):
            belt[i][j] = belt[i][j-1]

    for i in range(3):
        belt[i][0] = last_numbers[(i-1)%3]

for i in range(3):
    print(' '.join(belt[i]))