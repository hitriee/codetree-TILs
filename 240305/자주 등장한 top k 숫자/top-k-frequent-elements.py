n, k = map(int, input().split())
numbers = tuple(map(int, input().split()))
frequency = {}

for number in numbers:
    if frequency.get(number):
        frequency[number] += 1
    else:
        frequency[number] = 1

sorted_nums = sorted(frequency.keys(), key=lambda key: (-frequency[key], -key))

print(*sorted_nums[:k])