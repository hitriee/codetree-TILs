from heapq import heappush, heappop, heapify

n = int(input())
numbers = list(map(lambda x: -int(x), input().split()))
heapify(numbers)

while len(numbers) >= 2:
    number1 = heappop(numbers)
    number2 = heappop(numbers)
    if number1 != number2:
        heappush(numbers, -abs(number1 - number2))

if len(numbers) == 1:
    print(-numbers[0])
else:
    print(-1)