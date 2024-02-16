n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = [numbers[0]]

print(numbers[0], end=' ')
for i in range(2, n, 2):
    for j in range(-1, 1):
        last = i+j
        number = numbers[last]
        sorted_numbers.append(number)
        for k in range(last-1, -1, -1):
            if sorted_numbers[k] > number:
                sorted_numbers[k], sorted_numbers[k+1] = sorted_numbers[k+1], sorted_numbers[k]
            else:
                break
    print(sorted_numbers[i//2], end=' ')