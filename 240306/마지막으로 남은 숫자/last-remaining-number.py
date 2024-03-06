from heapq import heappush, heappop, heapify

n = int(input())
numbers = list(map(lambda x: -int(x), input().split()))
heapify(numbers)

while n >= 2:
    number1 = heappop(numbers)
    number2 = heappop(numbers)
    if number1 != number2:
        heappush(numbers, -abs(number1 - number2))
        n -= 1
    else:
        n -= 2

print(-numbers[0] if n == 1 else -1)