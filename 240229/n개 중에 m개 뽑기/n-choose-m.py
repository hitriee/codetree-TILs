N, M = map(int, input().split())

def find_comb(level, result, start):
    if level == M:
        print(result)
        return
    
    for i in range(start, N+1):
        find_comb(level+1, result+f' {str(i)}', i+1)

for i in range(1, N+1):
    find_comb(1, str(i), i+1)