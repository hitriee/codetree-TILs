n, m = map(int, input().split())
A = list(map(int, input().split()))

numbers = []
max_val = 0

def choose_num(level, start):
    global max_val

    if level == m:
        result = numbers[0]
        for j in range(1, m):
            result ^= numbers[j]
        if result > max_val:
            max_val = result
        return

    for i in range(start, n):
        numbers.append(A[i])
        choose_num(level+1, i+1)
        numbers.pop()

choose_num(0, 0)
print(max_val)