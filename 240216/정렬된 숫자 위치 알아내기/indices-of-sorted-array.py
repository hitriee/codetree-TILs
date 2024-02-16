N = int(input())
numbers = list(enumerate(map(int, input().split())))
numbers.sort(lambda number: (number[1], number[0]))
order = [0] * N

for i in range(N):
    order[numbers[i][0]] = i+1

print(*order)