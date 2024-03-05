formula = input()
n = len(formula)
check = {}
max_val = -2**31
for i in range(0, n, 2):
    element = formula[i]
    if not check.get(element):
        check[element] = 0

def calc(result, operator, num):
    if operator == '+':
        result += num
    elif operator == '-':
        result -= num
    else:
        result *= num
    
    return result

def find_max(level, result):
    global max_val

    if level >= n:
        if max_val < result:
            max_val = result
        return
    
    operator, alp = formula[level:level+2]
    if check[alp]:
        result = calc(result, operator, check[alp])
        find_max(level+2, result)
    else:
        for i in range(1, 5):
            check[alp] = i
            value = calc(result, operator, i)
            find_max(level+2, value)
            check[alp] = 0

for i in range(1, 5):
    check[formula[0]] = i
    find_max(1, i)

print(max_val)