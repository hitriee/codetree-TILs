n = int(input())
numbers = list(map(int, input().split()))
min_num_arr = [0] * n
acc = list(numbers)
min_num = acc[-1] = numbers[-1]
max_avg = 0

for i in range(n-2, 0, -1):
    acc[i] += acc[i+1]
    if min_num > numbers[i]:
        min_num = numbers[i]
    min_num_arr[i] = min_num

for i in range(1, n-1):
    avg = (acc[i] - min_num_arr[i])/(n-i-1)
    if max_avg < avg:
        max_avg = avg

print(f'{max_avg :.2f}')