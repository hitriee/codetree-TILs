N, M = map(int, input().split())
str_nums = tuple(map(str, range(1, N+1)))
result = []

def find_comb(level, start):
    if level == M:
        print(' '.join(result))
        return
    
    for i in range(start, N):
        num = str_nums[i]
        result.append(num)
        find_comb(level+1, i+1)
        result.pop()

for i in range(N):
    num = str_nums[i]
    result.append(num)
    find_comb(1, i+1)
    result.pop()