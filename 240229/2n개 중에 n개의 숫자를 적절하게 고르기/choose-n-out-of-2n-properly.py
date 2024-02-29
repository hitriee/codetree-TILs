n = int(input())
numbers = tuple(map(int, input().split()))
min_dif = n * 1000
total = sum(numbers)

def split_numbers(level=0, result=0, start=0):
    global min_dif

    if level == n:
        dif = abs(total - 2*result)
        if min_dif > dif:
            min_dif = dif
        return
    
    for i in range(start, 2*n):
        split_numbers(level+1, result+numbers[i], i+1)

split_numbers()

print(min_dif)