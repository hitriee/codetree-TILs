K, N = map(int, input().split())
str_candidate = list(map(str, range(1, K+1)))

def choose_num(level, result):
    if level == N:
        print(result)
        return
    
    for num in str_candidate:
        choose_num(level+1, result+f' {num}')

for num in str_candidate:
    choose_num(1, num)