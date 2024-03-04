formula = input()
n = len(formula)
check = {}
limit, max_val = 0, -2**31
keys = []
for i in range(0, n, 2):
    element = formula[i]
    if not check.get(element):
        check[element] = 0
        limit += 1
        keys.append(element)

def calc():
    result = check[formula[0]]
    for i in range(1, n, 2):
        operator, alp = formula[i:i+2]
        num = check[alp]
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        else:
            result *= num
    return result

def find_max(level):
    global max_val

    if level == limit:
        value = calc()
        if max_val < value:
            max_val = value
        return
    
    for i in range(1, 5):
        check[keys[level]] = i
        find_max(level+1)

find_max(0)

print(max_val)