N, M = map(int, input().split())

# Please write your code here.
path = []
answer = []
def backtracking(level, cnt):
    if level == N:
        if cnt == M:
            answer.append(' '.join(path))
        return
    
    backtracking(level+1, cnt)

    path.append(str(level+1))
    backtracking(level+1, cnt+1)
    path.pop()

backtracking(0, 0)

print('\n'.join(answer[::-1]))
