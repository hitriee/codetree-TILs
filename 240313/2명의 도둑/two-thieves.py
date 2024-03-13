N, M, C = map(int, input().split())
weight_info = [list(map(int, input().split())) for _ in range(N)]
max_total = chosen_max = 0
acc = [[] for _ in range(N)]

for i in range(N):
    total = sum(weight_info[i][:M-1])
    for j in range(M-1, N):
        total += weight_info[i][j]
        acc[i].append(total)
        total -= weight_info[i][j-M+1]

def calc_value(arr):
    value = 0
    for num in arr:
        value += num * num
    return value

def choose(level, row, start, end, total, sq_total):
    global chosen_max
    if level == M:
        return
    
    for j in range(start, end):
        value = weight_info[row][j]
        new_total = total + value
        if new_total <= C:
            new_sq_total = sq_total + value * value
            if chosen_max < new_sq_total:
                chosen_max = new_sq_total
            choose(level+1, row, j+1, end, new_total, new_sq_total)


def find_max(i, j):
    global chosen_max

    if acc[i][j] <= C:
        return calc_value(weight_info[i][j:j+M])
    else:
        chosen_max = 0
        choose(0, i, j, j+M, 0, 0)
        return chosen_max


for i1 in range(N):
    for j1 in range(N-M):
        total = find_max(i1, j1)
        for j2 in range(j1+M, N-M+1):
            new_total = total + find_max(i1, j2)
            if max_total < new_total:
                max_total = new_total

        for i2 in range(i1+1, N):
            for j2 in range(N-M+1):
                new_total = total + find_max(i2, j2)
                if max_total < new_total:
                    max_total = new_total
        

print(max_total)