n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = [numbers[0]]

print(numbers[0], end=' ')
for i in range(2, n, 2):
    for j in range(-1, 1):
        last = i+j
        number = numbers[last]
        start, end = 0, last-1
        while start <= end:
            mid = (start+end)//2
            if sorted_numbers[mid] > number:
                end = mid - 1
            elif sorted_numbers[mid] < number:
                start = mid + 1
            else:
                sorted_numbers.insert(mid, number)
                break
        else:
            sorted_numbers.insert(start, number)
    
    print(sorted_numbers[i//2], end=' ')