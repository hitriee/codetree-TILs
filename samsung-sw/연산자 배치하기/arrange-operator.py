n = int(input())
numbers = list(map(int, input().split()))
possible = list(map(int, input().split()))

max_val, min_val = -int(1e9), int(1e9)

def calc(num1, num2, kind_of):
    if kind_of == 0:
        return num1 + num2
    elif kind_of == 1:
        return num1 - num2
    return num1 * num2

def dfs(level, val):
    global max_val, min_val

    if level == n:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
        return
    
    for i in range(3):
        if possible[i]:
            possible[i] -= 1
            new_val = calc(val, numbers[level], i)
            dfs(level+1, new_val)
            possible[i] += 1


dfs(1, numbers[0])

print(min_val, max_val)