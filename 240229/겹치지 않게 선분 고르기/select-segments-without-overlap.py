n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
max_cnt = 0
lines.sort()

def choose_lines(level, last, start):
    global max_cnt

    if max_cnt < level:
        max_cnt = level

    for i in range(start, n):
        s, e = lines[i]
        if s > last:
            choose_lines(level+1, e, i+1)

for i in range(n):
    choose_lines(1, lines[i][1], i+1)

print(max_cnt)