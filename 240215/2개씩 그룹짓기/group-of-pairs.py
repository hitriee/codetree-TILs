N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

left, right = 0, 2*N-1
max_total = 0
while left < right:
    total = numbers[left] + numbers[right]
    if max_total < total:
        max_total = total
    left += 1
    right -= 1

print(max_total)