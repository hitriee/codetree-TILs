from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
numbers = list(map(lambda x: -int(x), input().split()))
heapify(numbers)

for _ in range(m):
    number = heappop(numbers) + 1
    heappush(numbers, number)

print(-numbers[0])