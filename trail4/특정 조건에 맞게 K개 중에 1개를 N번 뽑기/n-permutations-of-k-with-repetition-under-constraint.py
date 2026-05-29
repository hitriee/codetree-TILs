K, N = map(int, input().split())

# Please write your code here.
path = []
def backtracking(level, cnt):
    if cnt >= 3:
        return
    if level == N:
        print(*path)
        return
    
    new_level = level+1
    
    for i in range(1, K+1):
        if level == 0 or path[-1] != i:
            new_cnt = 1
        elif cnt < 2:
            new_cnt = cnt + 1
        else:
            continue

        path.append(i)
        backtracking(new_level, new_cnt)
        path.pop()


backtracking(0, 1)
