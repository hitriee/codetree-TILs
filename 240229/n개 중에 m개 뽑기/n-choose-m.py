N, M = map(int, input().split())
str_nums = tuple(map(str, range(1, N+1)))

def find_comb(level, result, start):
    if level == M:
        print(result)
        return
    
    for i in range(start, N):
        num = str_nums[i]
        find_comb(level+1, result+f' {num}', i+1)

for i in range(N):
    num = str_nums[i]
    find_comb(1, num, i+1)