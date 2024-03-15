n = int(input())
numbers = list(map(int, input().split()))
total = 0
for i in range(n):
    total += numbers[i]
    if total > 200:
        print(total)
        print(f'{total//(i+1) :.1f}')
        break