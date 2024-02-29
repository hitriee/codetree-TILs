n, m = map(int, input().split())
max_result = 0
numbers = tuple(map(int, input().split()))

def calc_nums(level=0, start=0, result=0):
    global max_result

    if level == m:
        if max_result < result:
            max_result = result
        return
    
    for i in range(start, n):
        calc_nums(level+1, i+1, result^i)

for i in range(n):
    calc_nums(1, i+1, i)

print(max_result)