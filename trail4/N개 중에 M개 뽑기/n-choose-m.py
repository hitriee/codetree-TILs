N, M = map(int, input().split())

# Please write your code here.
path = []
def backtracking(level, start):
    if level == M:
        print(*path)
        return
    
    for i in range(start, N+1):
        path.append(i)
        backtracking(level+1, i+1)
        path.pop()

backtracking(0, 1)
