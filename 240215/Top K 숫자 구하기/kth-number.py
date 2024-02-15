from heapq import heapify, heappop
N, k = map(int, input().split())
numbers = list(map(int, input().split()))
heapify(numbers)

for _ in range(k-1):
    heappop(numbers)

print(numbers[0])