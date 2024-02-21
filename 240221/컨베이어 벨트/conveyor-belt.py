n, t = map(int, input().split())
numbers = input().split()
numbers += input().split()

for _ in range(t):
    last_number = numbers[-1]
    for i in range(2*n-1, 0, -1):
        numbers[i] = numbers[i-1]
    numbers[0] = last_number

print(' '.join(numbers[:n]))
print(' '.join(numbers[n:]))