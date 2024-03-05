n, k = map(int, input().split())
numbers = tuple(map(int, input().split()))
frequency = {}

for number in numbers:
    if frequency.get(number):
        frequency[number] += 1
    else:
        frequency[number] = 1

sorted_nums = sorted(frequency.items(), key=lambda x: (-x[1], -x[0]))

for i in range(k):
    print(sorted_nums[i][0], end=' ')