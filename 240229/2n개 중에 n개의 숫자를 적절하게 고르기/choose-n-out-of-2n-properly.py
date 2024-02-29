n = int(input())
numbers = tuple(map(int, input().split()))
min_dif = n * 1000
total = sum(numbers)
twice = 2*n

def split_numbers(level, result, start):
    global min_dif

    if level == n:
        dif = abs(total - 2*result)
        if min_dif > dif:
            min_dif = dif
        return
    
    for i in range(start, twice):
        split_numbers(level+1, result+numbers[i], i+1)

split_numbers(0, 0, 0)

print(min_dif)