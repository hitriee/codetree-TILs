from heapq import heapify, heappush, heappop

n = int(input())
numbers = list(map(int, input().split()))
heapify(numbers)
min_cost = 0

while n > 1:
    num1 = heappop(numbers)
    num2 = heappop(numbers)
    cost = num1 + num2
    min_cost += cost
    heappush(numbers, cost)
    n -= 1

print(min_cost)